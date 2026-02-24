# Experiment No. 04
## Design GUI Components Using Database in Android Studio

**Aim:**
Design and develop an Android application to perform database operations (Insert and View records) using SQLite.

**Prerequisite:**
- Object Oriented Programming Language (Java)

**Course Outcome:**
Upon completing this experiment, students will be able to develop and demonstrate mobile applications using various tools.

**Software used:**
- Android Studio
- JDK
- Android SDK
- Emulator or Android Device
- SQLite Database

---

### Theory

SQLite is a lightweight, embedded relational database engine that ships with every Android device. It requires no separate installation or server process — Android exposes it through the `SQLiteOpenHelper` and `SQLiteDatabase` APIs.

In this experiment, a user registration form collects Name, Email, Contact Number, and Gender. The data is persisted into a local SQLite database and displayed in a scrollable list using `RecyclerView`.

#### Module Overview

| Module                       | Responsibility                                                 |
|-----------------------------|----------------------------------------------------------------|
| `FirstActivity`             | Collects input, validates fields, inserts data into SQLite     |
| `SecondActivity`            | Retrieves all records and displays them via `RecyclerView`     |
| `DatabaseHelper`            | Manages database creation, insertion, and retrieval            |
| `ModelForUsers`             | POJO data model with getters and setters                       |
| `UserRecyclerViewAdapter`   | Binds user data to `RecyclerView` item views                   |

#### Key Android Database APIs:
- **`SQLiteOpenHelper`** — Abstract class that manages database creation and version management.
- **`SQLiteDatabase`** — Provides methods for CRUD operations (`insert()`, `query()`, `update()`, `delete()`).
- **`Cursor`** — Iterator that traverses query result rows.
- **`ContentValues`** — Key-value container for inserting row data.

---

### Procedure

1. Install Android Studio with Android SDK and emulator.
2. Create a new project → Empty Activity → Name: **Database_Operations**, Package: `com.example.database_operations`, Language: Java.
3. Add dependencies in `build.gradle`:
   - `androidx.recyclerview:recyclerview:1.3.2`
   - `com.google.android.material:material:1.11.0`
4. Create Java classes: `FirstActivity`, `SecondActivity`, `DatabaseHelper`, `ModelForUsers`, `UserRecyclerViewAdapter`.
5. Create XML layouts: `activity_first.xml`, `activity_second.xml`, `row_users.xml`.
6. Configure `AndroidManifest.xml` with both activities.
7. Run the application on an emulator or device.

---

### Tasks

Develop an Android application that allows users to enter, store, and view user details using an SQLite database. The application should validate user input, insert records into the database, and display all stored records using a RecyclerView.

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

**File: `activity_first.xml`**

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="24dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="User Registration"
        android:textSize="22sp"
        android:textStyle="bold"
        android:layout_marginBottom="16dp" />

    <com.google.android.material.textfield.TextInputLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp">
        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/etName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Name"
            android:inputType="text" />
    </com.google.android.material.textfield.TextInputLayout>

    <com.google.android.material.textfield.TextInputLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp">
        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/etEmail"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Email"
            android:inputType="textEmailAddress" />
    </com.google.android.material.textfield.TextInputLayout>

    <com.google.android.material.textfield.TextInputLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp">
        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/etContact"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Contact Number"
            android:inputType="phone" />
    </com.google.android.material.textfield.TextInputLayout>

    <RadioGroup
        android:id="@+id/rgGender"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:layout_marginBottom="16dp">

        <RadioButton
            android:id="@+id/rbMale"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Male" />

        <RadioButton
            android:id="@+id/rbFemale"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Female" />
    </RadioGroup>

    <Button
        android:id="@+id/btnInsert"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Insert Data"
        android:layout_marginBottom="8dp" />

    <Button
        android:id="@+id/btnViewUsers"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="View Users" />

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
    android:padding="16dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="All Users"
        android:textSize="22sp"
        android:textStyle="bold"
        android:layout_marginBottom="16dp" />

    <TextView
        android:id="@+id/tvNoData"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="No user details available"
        android:textSize="16sp"
        android:visibility="gone" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/rvUsers"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</LinearLayout>
```

---

**File: `row_users.xml`**

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_margin="8dp"
    app:cardCornerRadius="8dp"
    app:cardElevation="4dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="16dp">

        <TextView
            android:id="@+id/tvId"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/tvName"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content" />

        <TextView
            android:id="@+id/tvEmail"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content" />

        <TextView
            android:id="@+id/tvContact"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content" />

        <TextView
            android:id="@+id/tvGender"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content" />

    </LinearLayout>

</androidx.cardview.widget.CardView>
```

---

**File: `ModelForUsers.java`**
> Package name: `com.example.database_operations`

```java
package com.example.database_operations;

public class ModelForUsers {
    private int id;
    private String name, email, contactNo, gender;

    public ModelForUsers(int id, String name, String email, String contactNo, String gender) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.contactNo = contactNo;
        this.gender = gender;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public String getContactNo() { return contactNo; }
    public String getGender() { return gender; }
}
```

---

**File: `DatabaseHelper.java`**
> Package name: `com.example.database_operations`

```java
package com.example.database_operations;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import java.util.ArrayList;

public class DatabaseHelper extends SQLiteOpenHelper {

    private static final String DB_NAME = "UsersDB";
    private static final int DB_VERSION = 1;
    private static final String TABLE_NAME = "Users";

    public DatabaseHelper(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String query = "CREATE TABLE " + TABLE_NAME + " ("
                + "Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                + "Name TEXT, "
                + "Email TEXT, "
                + "Contact_No TEXT, "
                + "Gender TEXT)";
        db.execSQL(query);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    public boolean insertUserDetails(String name, String email, String contactNo, String gender) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put("Name", name);
        values.put("Email", email);
        values.put("Contact_No", contactNo);
        values.put("Gender", gender);
        long result = db.insert(TABLE_NAME, null, values);
        db.close();
        return result != -1;
    }

    public ArrayList<ModelForUsers> getAllUserDetails() {
        ArrayList<ModelForUsers> list = new ArrayList<>();
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLE_NAME, null);

        if (cursor.moveToFirst()) {
            do {
                list.add(new ModelForUsers(
                        cursor.getInt(0),
                        cursor.getString(1),
                        cursor.getString(2),
                        cursor.getString(3),
                        cursor.getString(4)));
            } while (cursor.moveToNext());
        }
        cursor.close();
        db.close();
        return list;
    }
}
```

---

**File: `UserRecyclerViewAdapter.java`**
> Package name: `com.example.database_operations`

```java
package com.example.database_operations;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;

public class UserRecyclerViewAdapter extends RecyclerView.Adapter<UserRecyclerViewAdapter.ViewHolder> {

    private ArrayList<ModelForUsers> userList;

    public UserRecyclerViewAdapter(ArrayList<ModelForUsers> userList) {
        this.userList = userList;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.row_users, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        ModelForUsers user = userList.get(position);
        holder.tvId.setText("ID: " + user.getId());
        holder.tvName.setText("Name: " + user.getName());
        holder.tvEmail.setText("Email: " + user.getEmail());
        holder.tvContact.setText("Contact: " + user.getContactNo());
        holder.tvGender.setText("Gender: " + user.getGender());
    }

    @Override
    public int getItemCount() {
        return userList.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvId, tvName, tvEmail, tvContact, tvGender;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            tvId = itemView.findViewById(R.id.tvId);
            tvName = itemView.findViewById(R.id.tvName);
            tvEmail = itemView.findViewById(R.id.tvEmail);
            tvContact = itemView.findViewById(R.id.tvContact);
            tvGender = itemView.findViewById(R.id.tvGender);
        }
    }
}
```

---

**File: `FirstActivity.java`**
> Package name: `com.example.database_operations`

```java
package com.example.database_operations;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioGroup;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.textfield.TextInputEditText;

public class FirstActivity extends AppCompatActivity {

    TextInputEditText etName, etEmail, etContact;
    RadioGroup rgGender;
    Button btnInsert, btnViewUsers;
    DatabaseHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first);

        etName = findViewById(R.id.etName);
        etEmail = findViewById(R.id.etEmail);
        etContact = findViewById(R.id.etContact);
        rgGender = findViewById(R.id.rgGender);
        btnInsert = findViewById(R.id.btnInsert);
        btnViewUsers = findViewById(R.id.btnViewUsers);
        dbHelper = new DatabaseHelper(this);

        btnInsert.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (validateForm()) {
                    String name = etName.getText().toString().trim();
                    String email = etEmail.getText().toString().trim();
                    String contact = etContact.getText().toString().trim();
                    String gender = rgGender.getCheckedRadioButtonId() == R.id.rbMale ? "Male" : "Female";

                    boolean success = dbHelper.insertUserDetails(name, email, contact, gender);
                    if (success) {
                        Toast.makeText(FirstActivity.this, "Data inserted successfully", Toast.LENGTH_SHORT).show();
                        etName.setText("");
                        etEmail.setText("");
                        etContact.setText("");
                        rgGender.clearCheck();
                    } else {
                        Toast.makeText(FirstActivity.this, "Insertion failed", Toast.LENGTH_SHORT).show();
                    }
                }
            }
        });

        btnViewUsers.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(FirstActivity.this, SecondActivity.class));
            }
        });
    }

    private boolean validateForm() {
        boolean valid = true;
        if (etName.getText().toString().trim().isEmpty()) {
            etName.setError("Name is required");
            valid = false;
        }
        if (etEmail.getText().toString().trim().isEmpty()) {
            etEmail.setError("Email is required");
            valid = false;
        }
        if (etContact.getText().toString().trim().isEmpty()) {
            etContact.setError("Contact is required");
            valid = false;
        }
        if (rgGender.getCheckedRadioButtonId() == -1) {
            Toast.makeText(this, "Please select gender", Toast.LENGTH_SHORT).show();
            valid = false;
        }
        return valid;
    }
}
```

---

**File: `SecondActivity.java`**
> Package name: `com.example.database_operations`

```java
package com.example.database_operations;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import java.util.ArrayList;

public class SecondActivity extends AppCompatActivity {

    RecyclerView rvUsers;
    TextView tvNoData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        rvUsers = findViewById(R.id.rvUsers);
        tvNoData = findViewById(R.id.tvNoData);

        DatabaseHelper dbHelper = new DatabaseHelper(this);
        ArrayList<ModelForUsers> userList = dbHelper.getAllUserDetails();

        if (userList.isEmpty()) {
            tvNoData.setVisibility(View.VISIBLE);
            rvUsers.setVisibility(View.GONE);
        } else {
            tvNoData.setVisibility(View.GONE);
            rvUsers.setVisibility(View.VISIBLE);
            rvUsers.setLayoutManager(new LinearLayoutManager(this));
            rvUsers.setAdapter(new UserRecyclerViewAdapter(userList));
        }
    }
}
```

---

**File: `AndroidManifest.xml`** *(relevant section)*

```xml
<activity android:name=".SecondActivity" />
<activity android:name=".FirstActivity" android:exported="true">
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

- The SQLite database (`UsersDB`) and the `Users` table are created automatically on the first launch of the application when `DatabaseHelper` is instantiated.
- User data is successfully inserted into the database after all form fields pass validation. A `Toast` message confirms the operation status.
- The `RadioGroup` correctly ensures single-selection for the Gender field; attempting to submit without selecting a gender triggers a `Toast` warning.
- `SecondActivity` retrieves all records using a `Cursor`-backed query and populates the `RecyclerView`. When no records exist, the "No user details available" `TextView` is shown instead.
- Each `RecyclerView` item is rendered using a `CardView` layout, displaying the user's ID, Name, Email, Contact Number, and Gender in a card format.

---

### Conclusions

This experiment demonstrates the integration of Android's GUI framework with the SQLite database engine for persistent local storage. The `SQLiteOpenHelper` abstraction simplifies database lifecycle management (creation, upgrade), while `ContentValues` and `Cursor` provide a clean API for data insertion and retrieval respectively. The use of `RecyclerView` with a custom adapter showcases the recommended approach for rendering dynamic lists efficiently, as it recycles view holders to minimise memory allocation. Overall, the experiment validates a complete data flow — from form input, through validation and persistence, to display — within a multi-activity Android application.

---

### Questions of Curiosity

**1. What is SQLite?**
SQLite is a self-contained, serverless, zero-configuration relational database engine. It stores the entire database as a single file on disk and is embedded directly into the application process, meaning there is no separate database server to manage.

**2. Why is SQLite used in Android?**
SQLite is bundled into the Android operating system, so it is available on every device without additional installation. It provides a lightweight, fast, and reliable mechanism for structured local storage — ideal for mobile apps where a full client-server database would be overkill.

**3. What is SQLiteOpenHelper?**
`SQLiteOpenHelper` is an abstract class that manages database creation and version management. Developers override `onCreate()` to define the initial schema and `onUpgrade()` to handle migrations when the database version changes, ensuring a clean lifecycle.

**4. What is a Cursor?**
A `Cursor` is an interface that provides random read-write access to the result set returned by a database query. It functions as an iterator — you call `moveToFirst()`, `moveToNext()`, etc. to traverse rows, and `getString()`, `getInt()` to extract column values.

**5. What is RecyclerView?**
`RecyclerView` is the modern replacement for `ListView`. It efficiently displays large datasets by recycling item views that scroll off-screen and rebinding them with new data. It requires a `LayoutManager` (e.g., `LinearLayoutManager`) and an `Adapter` to function.

**6. Difference between ListView and RecyclerView?**
| Aspect          | ListView                          | RecyclerView                                  |
|----------------|-----------------------------------|-----------------------------------------------|
| ViewHolder      | Optional (manual implementation)  | Enforced by the adapter pattern               |
| Layout Manager  | Only vertical scrolling           | Supports linear, grid, and staggered layouts  |
| Item Animation  | No built-in support               | Built-in `ItemAnimator` for add/remove/move   |
| Performance     | Less efficient with large lists   | View recycling is mandatory, more efficient   |

---

### References
1. Android Developers, *Canvas and Drawables*, Google Developers Documentation.
2. Android Developers, *Custom View Components*, Google Developers Documentation.
3. Meier, R., *Professional Android Application Development*, Wrox Publications.
