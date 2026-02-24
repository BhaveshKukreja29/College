# Experiment No. 03
## Design a Form Using GUI Components in Android Studio

**Aim:**
To design and implement a simple Login/Registration Form interface using various GUI components in Android Studio.

**Prerequisite:**
- Object Oriented Programming Language (Java)

**Course Outcome:**
Upon completing this experiment, students will be able to develop and demonstrate mobile applications using various tools.

**Software used:**
- Android Studio
- Java
- Android SDK
- Emulator or Android Device

---

### Theory

Android Studio is the official IDE for developing Android applications using Java and XML. In this experiment, a Login/Registration Form is designed to collect user details such as First Name, Last Name, Email, and Password, and to validate the entered data before proceeding further.

The user interface is designed using an XML layout file (`activity_main.xml`). A `LinearLayout` with vertical orientation arranges the GUI components sequentially. Multiple `EditText` components accept user input, where appropriate `inputType` attributes such as `text`, `textEmailAddress`, and `textPassword` ensure correct input formats. Two `Button` components — RESET and PROCEED — are provided to perform user actions.

The application logic is written in Java within the `MainActivity` class, which extends `AppCompatActivity`. The `onCreate()` method initialises the activity and connects the XML layout to the Java code using `setContentView()`. All GUI components are linked to their corresponding Java objects using `findViewById()`.

Event handling is implemented using `OnClickListener` for both buttons:
- The **PROCEED** button triggers a validation process through the `CheckAllFields()` method.
- The **RESET** button clears all input fields by setting their values to empty strings.

The `CheckAllFields()` method performs input validation by checking whether any text field is empty. If a field is found empty or if the password length is less than eight characters, an error message is displayed using `setError()`. A boolean variable tracks the validation status — only when all fields are correctly filled does the program allow navigation to another activity using an `Intent`.

#### GUI Components Used:
| Component               | Purpose                    |
|------------------------|----------------------------|
| `TextView`             | Display labels             |
| `EditText`             | Accept user input          |
| `RadioGroup/RadioButton` | Select options           |
| `CheckBox`             | Multiple-choice selections |
| `Button`               | Submit / Reset the form    |

---

### Procedure

1. Open Android Studio.
2. Create a new project → Select Empty Activity.
3. Name the project as **FormApp**.
4. Choose Java as the language.
5. Open `activity_main.xml`.
6. Add GUI components using XML.
7. Open `MainActivity.java`.
8. Write code to handle button click events.
9. Run the application on an emulator or real device.

---

### Tasks

Design and develop an Android application using Android Studio to create a Login/Registration Form. The application should provide a user interface containing input fields for First Name, Last Name, Email, and Password, along with RESET and PROCEED buttons. The application must validate user input to ensure that no field is left empty and that the password contains a minimum of eight characters. Appropriate error messages should be displayed for invalid inputs. Upon clicking the RESET button, all input fields should be cleared. The application should allow navigation to the next activity only after successful validation of all input fields.

---

> **Roll No.:** ___________
> **Name:** ___________
> **Program:** Mobile Computing Lab
> **Division:** C2
> **Semester:** 6
> **Batch:** C21
> **Date of Experiment:**
> **Date of Submission:**
> **Grade:**

---

### Program

**File: `activity_main.xml`**

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="24dp"
    android:gravity="center_horizontal">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Registration Form"
        android:textSize="24sp"
        android:textStyle="bold"
        android:layout_marginBottom="24dp" />

    <EditText
        android:id="@+id/etFirstName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="First Name"
        android:inputType="text"
        android:layout_marginBottom="12dp" />

    <EditText
        android:id="@+id/etLastName"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Last Name"
        android:inputType="text"
        android:layout_marginBottom="12dp" />

    <EditText
        android:id="@+id/etEmail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Email"
        android:inputType="textEmailAddress"
        android:layout_marginBottom="12dp" />

    <EditText
        android:id="@+id/etPassword"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Password (min 8 characters)"
        android:inputType="textPassword"
        android:layout_marginBottom="24dp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center">

        <Button
            android:id="@+id/btnReset"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="RESET"
            android:layout_marginEnd="8dp" />

        <Button
            android:id="@+id/btnProceed"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="PROCEED"
            android:layout_marginStart="8dp" />
    </LinearLayout>

</LinearLayout>
```

---

**File: `activity_second.xml`**

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="24dp"
    android:gravity="center">

    <TextView
        android:id="@+id/tvWelcome"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Welcome!"
        android:textSize="28sp"
        android:textStyle="bold" />

</LinearLayout>
```

---

**File: `MainActivity.java`**
> Package name: `com.example.formapp`

```java
package com.example.formapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText etFirstName, etLastName, etEmail, etPassword;
    Button btnReset, btnProceed;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etFirstName = findViewById(R.id.etFirstName);
        etLastName = findViewById(R.id.etLastName);
        etEmail = findViewById(R.id.etEmail);
        etPassword = findViewById(R.id.etPassword);
        btnReset = findViewById(R.id.btnReset);
        btnProceed = findViewById(R.id.btnProceed);

        btnProceed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (CheckAllFields()) {
                    Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                    intent.putExtra("name", etFirstName.getText().toString());
                    startActivity(intent);
                }
            }
        });

        btnReset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                etFirstName.setText("");
                etLastName.setText("");
                etEmail.setText("");
                etPassword.setText("");
            }
        });
    }

    private boolean CheckAllFields() {
        boolean valid = true;

        if (etFirstName.getText().toString().isEmpty()) {
            etFirstName.setError("First Name is required");
            valid = false;
        }
        if (etLastName.getText().toString().isEmpty()) {
            etLastName.setError("Last Name is required");
            valid = false;
        }
        if (etEmail.getText().toString().isEmpty()) {
            etEmail.setError("Email is required");
            valid = false;
        }
        if (etPassword.getText().toString().isEmpty()) {
            etPassword.setError("Password is required");
            valid = false;
        } else if (etPassword.getText().toString().length() < 8) {
            etPassword.setError("Password must be at least 8 characters");
            valid = false;
        }

        return valid;
    }
}
```

---

**File: `SecondActivity.java`**
> Package name: `com.example.formapp`

```java
package com.example.formapp;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        TextView tvWelcome = findViewById(R.id.tvWelcome);
        String name = getIntent().getStringExtra("name");
        tvWelcome.setText("Welcome, " + name + "!");
    }
}
```

---

**File: `AndroidManifest.xml`** *(relevant section)*

```xml
<activity android:name=".SecondActivity" />
<activity android:name=".MainActivity" android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- All `EditText` fields accept user input according to their specified `inputType` attributes (`text`, `textEmailAddress`, `textPassword`).
- When the PROCEED button is clicked with empty fields, appropriate error messages are displayed inline below each respective field using `setError()`.
- The password field enforces a minimum length of eight characters, displaying a distinct error message when the constraint is violated.
- Clicking the RESET button clears all four input fields simultaneously by setting their text to empty strings.
- Upon successful validation, the application transitions to `SecondActivity` via an `Intent`, confirming that activity navigation works only after all fields pass validation.

---

### Conclusions

This experiment demonstrates the construction of an interactive Login/Registration Form on Android using core GUI components. The `EditText` widget, combined with appropriate `inputType` attributes, ensures type-safe data entry, while the `setError()` mechanism provides immediate, contextual feedback to the user. The separation of UI definition (XML) from application logic (Java) adheres to the MVC pattern, and the use of explicit `Intent` for activity transitions showcases Android's navigation model. Overall, the experiment validates that Android's native widget toolkit is sufficient for building robust, validated data-entry forms.

---

### Questions of Curiosity

**1. What is the use of EditText?**
`EditText` is an Android widget that provides an editable text field. It extends `TextView` and allows the user to type input directly. Attributes such as `inputType` can restrict the kind of input accepted (e.g., email, password, number).

**2. Why is inputType used in EditText?**
The `inputType` attribute specifies the type of data the user is expected to enter. It controls two things: the soft keyboard layout shown to the user (e.g., an `@` key for email) and the display format (e.g., masking characters for passwords). This improves both usability and input correctness.

**3. What is the function of a Button in Android?**
A `Button` is a clickable UI component that triggers an action when pressed. It is typically used to submit forms, navigate between activities, or invoke any method bound through an event listener.

**4. What is an OnClickListener?**
`OnClickListener` is an interface in the `android.view.View` class. It defines a single callback method `onClick(View v)` that is invoked when the user taps the associated view. It is the standard mechanism for handling click events on buttons and other interactive elements.

**5. What is input validation?**
Input validation is the process of verifying that user-supplied data meets predefined criteria before the application processes it. Common checks include non-empty fields, minimum/maximum length, format matching (e.g., email regex), and data-type enforcement. It prevents erroneous or malicious data from reaching the backend.

**6. What happens when the RESET button is clicked?**
The `OnClickListener` bound to the RESET button calls `setText("")` on all four `EditText` fields, effectively clearing every input field and restoring the form to its initial blank state.

**7. What is the role of LinearLayout?**
`LinearLayout` is a view group that arranges its child views in a single direction — either horizontally or vertically. It provides a simple, predictable stacking model, and supports `layout_weight` for proportional sizing of child elements.

---

### References
1. Android Developers, *Canvas and Drawables*, Google Developers Documentation.
2. Android Developers, *Custom View Components*, Google Developers Documentation.
3. Meier, R., *Professional Android Application Development*, Wrox Publications.
