# Experiment No. 01
## Implementation of Basic 2D Graphical Primitives

**Aim:**
To design and implement fundamental 2D graphical primitives including point, line, rectangle, circle, and polygon using Android Studio.

**Prerequisite:**
- Object Oriented Programming Language

**Course Outcome:**
Upon completing this experiment, students will gain hands-on experience in developing and demonstrating mobile applications using various development tools.

**Software used:**
- Android Studio
- Java
- Android SDK
- Emulator or Android Device

---

### Theory

2D graphical primitives serve as foundational elements for constructing complex visual graphics. Android provides the `Canvas` and `Paint` classes for 2D graphics rendering:

- **Canvas** – Offers various methods for drawing shapes onto the screen.
- **Paint** – Specifies the visual attributes such as color, stroke width, style, and text size.

#### Common 2D Primitives:
| Primitive  | Method Used       |
|-----------|-------------------|
| Point     | `drawPoint()`     |
| Line      | `drawLine()`      |
| Rectangle | `drawRect()`      |
| Circle    | `drawCircle()`    |
| Polygon   | `drawPath()`      |

---

### Procedure

1. Launch Android Studio and create a new project.
2. Choose Empty Activity as the template.
3. Set Java as the programming language.
4. Implement a custom View class.
5. Override the `onDraw(Canvas canvas)` method.
6. Utilize `Paint` and `Canvas` methods to render 2D primitives.
7. Execute the application on an emulator or a connected device.

---

### Tasks

**Task 1: Create Android Project**
- Start a new Android project in Android Studio, select Empty Activity, and configure the project name, package, and SDK.

**Task 2: Set Up Main Activity**
- Create `MainActivity.java` and set the custom View as the content view via `setContentView()`.

**Task 3: Create Custom View Class**
- Define a class `MyView` extending `View` and initialize the `Paint` object inside the constructor.

**Task 4: Override onDraw()**
- Override `onDraw(Canvas canvas)` to prepare the canvas for drawing.

**Task 5: Draw Point**
- Configure paint color and stroke width, then invoke `drawPoint()` at the desired coordinates.

**Task 6: Draw Line**
- Update paint color and use `drawLine()` to render a straight line between two endpoints.

**Task 7: Draw Rectangle**
- Set the paint style to `STROKE` and call `drawRect()` with the specified boundaries.

**Task 8: Draw Circle**
- Assign a suitable paint color and use `drawCircle()` with a defined centre and radius.

**Task 9: Draw Polygon**
- Construct a `Path` object, define polygon vertices with `moveTo()` and `lineTo()`, close the path, and render it via `drawPath()`.

**Task 10: Execute and Verify**
- Run the app on an emulator or physical device and ensure all primitives render correctly.

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

#### Project: HelloWorld

**File: `MyActivity.java`**
> Package name: `com.example.maple`

```java
package com.example.maple;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MyActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);
    }
}
```

---

#### Project: 2dGraphics

**File: `MainActivity.java`**
> Package name: `com.example.graphics2d`

```java
package com.example.graphics2d;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(new MyView(this));
    }
}
```

**File: `MyView.java`**
> Package name: `com.example.graphics2d`

```java
package com.example.graphics2d;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.view.View;

public class MyView extends View {

    Paint paint;

    public MyView(Context context) {
        super(context);
        paint = new Paint();
        paint.setAntiAlias(true);
        paint.setStrokeWidth(5);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);

        // Point
        paint.setColor(Color.RED);
        canvas.drawPoint(120, 120, paint);

        // Line
        paint.setColor(Color.BLUE);
        canvas.drawLine(170, 170, 420, 170, paint);

        // Rectangle
        paint.setColor(Color.GREEN);
        paint.setStyle(Paint.Style.STROKE);
        canvas.drawRect(120, 220, 420, 380, paint);

        // Circle
        paint.setColor(Color.MAGENTA);
        canvas.drawCircle(270, 520, 110, paint);

        // Polygon (Triangle)
        paint.setColor(Color.BLACK);
        Path path = new Path();
        path.moveTo(120, 720);
        path.lineTo(320, 720);
        path.lineTo(220, 570);
        path.close();
        canvas.drawPath(path, paint);
    }
}
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

- The Android coordinate system places its origin at the top-left corner, with the x-axis running rightward and the y-axis running downward.
- A single `Paint` instance was initialised in the constructor and reused across all shapes. By dynamically modifying properties like `setColor()` and `setStyle()` within `onDraw()`, we minimise the memory footprint rather than instantiating separate `Paint` objects for each shape.

---

### Conclusions

Through this experiment, we successfully rendered a Hello World application and explored the fundamentals of 2D graphics rendering on Android using the `Canvas` and `Paint` APIs. The `onDraw()` method serves as the central callback for all rendering logic, where `Canvas` acts as the drawing surface and `Paint` governs visual attributes like color, style, and stroke width.

---

### Questions of Curiosity

**1. What is the use of the Canvas class?**
The `Canvas` class provides a programmable drawing surface that allows the developer to render shapes, paths, text, and images directly onto the screen.

**2. How are polygons drawn in Android?**
Polygons are constructed by defining a `Path` object with the desired vertices using `moveTo()` and `lineTo()`, closing the shape, and then drawing the path onto the `Canvas` using a configured `Paint` object.

**3. What is the role of onDraw() method?**
`onDraw()` is the framework callback invoked whenever the view needs to be rendered. The system supplies a `Canvas` instance, and the developer places all drawing commands inside this method.

---

### References
1. Android Developers, *Canvas and Drawables*, Google Developers Documentation.
2. Android Developers, *Custom View Components*, Google Developers Documentation.
3. Meier, R., *Professional Android Application Development*, Wrox Publications.
