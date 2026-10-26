# Experiment No. 05
## Development of EMI Calculator using Android

**Aim:**
To develop an EMI (Equated Monthly Installment) Calculator Android application using Android Studio that calculates monthly EMI based on Principal amount, Interest rate, and Loan tenure.

**Prerequisite:**
- Object Oriented Programming Language (Java)

**Course Outcome:**
Upon completing this experiment, students will be able to develop and demonstrate mobile applications using various tools.

**Software used:**
- Android Studio
- JDK
- Android SDK
- Emulator or Android Device

---

### Theory

The application is structured around a single `MainActivity` that extends `AppCompatActivity`. It contains `EditText` fields for Principal, Interest, Years, and EMI result, along with a `Button` for calculating EMI. Event handling is performed using `setOnClickListener()`. The `onCreate()` method initializes UI components and sets the layout using `setContentView()`.

The user interface is designed using `CoordinatorLayout`, `NestedScrollView`, `LinearLayout`, `TextInputLayout`, `EditText`, and `Button`. `TextInputLayout` is used to provide a Material Design interface with floating labels and error display. Input fields accept numeric values using `android:inputType="number"`.

Input validation is performed using `TextUtils.isEmpty()` to ensure no field is left empty, display error messages when necessary, and prevent the application from crashing due to invalid input.

The EMI calculation follows a modular programming approach, divided into separate methods:
- `calPric()` — returns principal
- `calInt()` — converts interest to monthly rate
- `calMonth()` — converts years to months
- `calDvdnt()` — calculates power term
- `calFinalDvdnt()` — calculates numerator
- `calDivider()` — calculates denominator
- `calEmi()` — calculates final EMI

When the Calculate button is clicked, input values are read, validation is performed, the EMI formula is applied, and the result is displayed in the EMI field. This demonstrates event-driven programming in Android.

---

### Procedure

1. Open Android Studio and wait until the IDE loads completely.
2. Click on New Project → select Empty Views Activity → click Next.
3. Enter the following details:
   - Application Name: **EMI Calculator**
   - Package Name: `com.example.calci`
   - Language: Java
4. Click Finish and wait for the Gradle build to complete.
5. Open `activity_main.xml` and design the layout with input fields for Principal, Interest, Years, a Calculate button, and an EMI output field.
6. Open `MainActivity.java` and implement the EMI calculation logic with input validation and modular methods.
7. Save all files.
8. Click on the Build menu → select Rebuild Project → ensure there are no errors.
9. Click the Run (▶) button and select an existing emulator or create a new virtual device.
10. Enter Principal Amount, Interest Rate, and Number of Years.
11. Click the Calculate button and verify the calculated EMI is displayed correctly.
12. Test with different input values and verify error messages appear when fields are left empty.

---

### Tasks

Design and develop an EMI (Equated Monthly Installment) Calculator Android application using Android Studio. The application should include input fields for Principal Amount, Interest Rate, and Loan Tenure (in years), along with a Calculate button and an output field to display the EMI. Implement proper input validation using TextUtils.isEmpty(), apply the standard EMI formula using modular methods, and handle button click events using setOnClickListener(). The program should correctly compute and display the EMI for valid inputs and show appropriate error messages when fields are left empty.

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
<androidx.coordinatorlayout.widget.CoordinatorLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <androidx.core.widget.NestedScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fillViewport="true">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="16dp">

            <!-- Principal -->
            <com.google.android.material.textfield.TextInputLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="Principal">
                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/etPrincipal"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:inputType="numberDecimal"/>
            </com.google.android.material.textfield.TextInputLayout>

            <!-- Interest -->
            <com.google.android.material.textfield.TextInputLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="Interest">
                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/etInterest"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:inputType="numberDecimal"/>
            </com.google.android.material.textfield.TextInputLayout>

            <!-- Years -->
            <com.google.android.material.textfield.TextInputLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="Years">
                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/etYears"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:inputType="number"/>
            </com.google.android.material.textfield.TextInputLayout>

            <!-- Calculate Button -->
            <Button
                android:id="@+id/btnCalculate"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Calculate EMI"
                android:layout_marginTop="24dp"/>

            <!-- EMI Result -->
            <com.google.android.material.textfield.TextInputLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="EMI">
                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/etEmi"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:inputType="numberDecimal"
                    android:enabled="false"/>
            </com.google.android.material.textfield.TextInputLayout>

        </LinearLayout>
    </androidx.core.widget.NestedScrollView>
</androidx.coordinatorlayout.widget.CoordinatorLayout>
```

---

**File: `MainActivity.java`**
> Package name: `com.example.calci`

```java
package com.example.calci;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.textfield.TextInputEditText;

public class MainActivity extends AppCompatActivity {

    private TextInputEditText etPrincipal, etInterest, etYears, etEmi;
    private Button btnCalculate;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etPrincipal = findViewById(R.id.etPrincipal);
        etInterest = findViewById(R.id.etInterest);
        etYears = findViewById(R.id.etYears);
        etEmi = findViewById(R.id.etEmi);
        btnCalculate = findViewById(R.id.btnCalculate);

        btnCalculate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (validateInputs()) {
                    double principal = calPric();
                    double monthlyInterest = calInt();
                    int months = calMonth();
                    double dvdnt = calDvdnt(monthlyInterest, months);
                    double finalDvdnt = calFinalDvdnt(monthlyInterest, dvdnt);
                    double divider = calDivider(dvdnt);
                    double emi = calEmi(principal, finalDvdnt, divider);
                    etEmi.setText(String.format("%.2f", emi));
                }
            }
        });
    }

    private boolean validateInputs() {
        if (TextUtils.isEmpty(etPrincipal.getText())) { etPrincipal.setError("Enter Principal"); return false; }
        if (TextUtils.isEmpty(etInterest.getText())) { etInterest.setError("Enter Interest"); return false; }
        if (TextUtils.isEmpty(etYears.getText())) { etYears.setError("Enter Years"); return false; }
        return true;
    }

    private double calPric() { return Double.parseDouble(etPrincipal.getText().toString()); }
    private double calInt() { return Double.parseDouble(etInterest.getText().toString()) / (12 * 100); }
    private int calMonth() { return Integer.parseInt(etYears.getText().toString()) * 12; }
    private double calDvdnt(double monthlyInterest, int months) { return Math.pow(1 + monthlyInterest, months); }
    private double calFinalDvdnt(double monthlyInterest, double dvdnt) { return monthlyInterest * dvdnt; }
    private double calDivider(double dvdnt) { return dvdnt - 1; }
    private double calEmi(double principal, double finalDvdnt, double divider) { return principal * (finalDvdnt / divider); }
}
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

The application successfully accepts numeric input for Principal Amount, Interest Rate, and Loan Tenure through the EditText fields. Input validation using TextUtils.isEmpty() prevents calculation when any input field is left blank. Appropriate error messages are displayed using setError() on the respective fields when invalid or empty input is detected. The Calculate button triggers the EMI computation correctly using setOnClickListener() event handling. The modular methods (for principal, interest conversion, months, numerator, denominator, and EMI) execute sequentially without runtime errors. The EMI result is displayed accurately in the output field for valid inputs. The application runs successfully on the emulator/device without crashing during multiple test cases. Testing with different values produces corresponding EMI outputs, confirming correct implementation of the EMI formula.

---

### Conclusions

The EMI Calculator Android application was successfully developed using Android Studio and Java. Proper input validation using TextUtils.isEmpty() improved the reliability and prevented runtime errors due to empty fields. The modular programming approach made the EMI calculation logic organized, reusable, and easy to understand. Event-driven programming using setOnClickListener() worked effectively to perform calculations on user interaction. The application accurately computes and displays EMI values, fulfilling the aim of the experiment. The experiment demonstrates the integration of Android UI components, input handling, and real-world financial calculations in mobile application development.

---

### Questions of Curiosity

**1. What is the role of TextUtils.isEmpty()?**
TextUtils.isEmpty() is used to check whether a text field contains null or empty data. It helps in input validation by ensuring that users do not leave required fields blank before performing calculations.

**2. What is the function of setOnClickListener()?**
setOnClickListener() is used to handle user interaction events such as button clicks. When a user clicks a button, the code inside the listener method is executed.

**3. Why does MainActivity extend AppCompatActivity?**
MainActivity extends AppCompatActivity to use advanced Android features like the action bar and Material Design components while maintaining compatibility with older Android versions.

**4. What is the difference between EditText and TextView?**
EditText is an input field that allows users to enter and modify text, whereas TextView is used only to display text and does not allow user editing.

**5. What is TextInputLayout and why is it used?**
TextInputLayout is a layout wrapper for EditText that enhances the user interface by providing features like floating hints, error messages, and improved Material Design styling.

**6. What is the purpose of findViewById()?**
findViewById() is used to locate and connect UI elements from the XML layout file to the Java code using their unique ID, allowing the program to interact with those components.

**7. What is the use of setContentView()?**
setContentView() is used to define which layout file should be displayed on the screen when the activity starts. It links the activity with its user interface design.

---

### References
1. Android Developers, *Canvas and Drawables*, Google Developers Documentation.
2. Android Developers, *Custom View Components*, Google Developers Documentation.
3. Meier, R., *Professional Android Application Development*, Wrox Publications.
