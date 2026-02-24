# Experiment No. 02
## Implementation of Basic 3D Graphical Primitives

**Aim:**
To design and implement basic 3D graphical primitives such as a cube and cuboid using Android Studio.

**Prerequisite:**
- Object Oriented Programming Language (Java)

**Course Outcome:**
Upon completing this experiment, students will gain practical experience in building and demonstrating mobile applications using various development tools.

**Software used:**
- Android Studio
- Java
- Android SDK
- Emulator or Android Device

---

### Theory

A `Bitmap` is instantiated to serve as the off-screen drawing surface. This bitmap is then assigned as the image source of an `ImageView`, allowing all drawn elements to be visible on the screen. A `Canvas` object is associated with the bitmap, providing methods to render shapes, lines, and text.

The `Paint` class defines drawing attributes such as color and text size. Separate `Paint` objects are used for the cube and cuboid so they can be visually distinguished by color. Using `drawLine()`, multiple straight-line segments are rendered to form the edges of each shape. The 3D illusion is achieved by offsetting the back face from the front face and connecting corresponding corners.

Text labels are placed using `drawText()` to identify each primitive. The coordinates provided to the drawing methods determine the position and size of all shapes on the screen. This approach demonstrates how 3D primitives can be represented on a 2D display by leveraging `Bitmap`, `Canvas`, and `Paint`.

---

### Procedure

1. Open Android Studio.
2. Click New Project → select Empty Activity.
3. Set the application name as **Primitives3D** and package name as `com.example.primitives3d`.
4. Choose Java as the language and select minimum SDK API 21 (Android 5.0) or higher.
5. Click Finish.
6. Open `MainActivity.java` and replace the boilerplate code with the given program that uses `Bitmap`, `Canvas`, and `Paint` to draw 3D primitives.
7. Open `activity_main.xml` and add an `ImageView` with id `imageView`.
8. Save all files and resolve any syntax errors.
9. Connect an Android device via USB or launch the Android Emulator.
10. Click Run and select the target device.
11. Observe the output — a cube and cuboid rendered via line drawings.

---

### Tasks

**Task 1: Create Android Project**
- Create a new Android project, select Empty Activity, and configure the project name, package name, and SDK version.

**Task 2: Set Up Main Activity**
- Create `MainActivity.java` and set the layout using `setContentView(R.layout.activity_main)`.

**Task 3: Design Layout with ImageView**
- Open `activity_main.xml`, add an `ImageView` to host the bitmap graphic, and assign it an `id`.

**Task 4: Create Bitmap and Canvas**
- Instantiate a `Bitmap` as the drawing surface and attach a `Canvas` object to it.

**Task 5: Initialize Paint Objects**
- Create `Paint` instances and configure color and text size for drawing shapes and labels.

**Task 6: Draw Cuboid**
- Use `drawLine()` to draw the front face, the offset back face, and the connecting edges to achieve the 3D cuboid effect.

**Task 7: Label the Cuboid**
- Apply paint properties for text and call `drawText()` to display the label "Cuboid".

**Task 8: Draw Cube**
- Use `drawLine()` to draw the front and back faces and connecting edges to form a 3D cube.

**Task 9: Label the Cube**
- Use `drawText()` to display the label "Cube" at an appropriate position.

**Task 10: Set Bitmap to ImageView**
- Assign the bitmap to the `ImageView` to display the rendered graphics.

**Task 11: Execute and Verify**
- Run the app on an emulator or device and verify that the cube and cuboid display correctly.

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
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

</RelativeLayout>
```

**File: `MainActivity.java`**
> Package name: `com.example.primitives3d`

```java
package com.example.primitives3d;

import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.widget.ImageView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView imageView = findViewById(R.id.imageView);

        Bitmap bitmap = Bitmap.createBitmap(1000, 1400, Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        canvas.drawColor(Color.WHITE);

        // Paint for cuboid
        Paint cuboidPaint = new Paint();
        cuboidPaint.setColor(Color.BLUE);
        cuboidPaint.setStrokeWidth(4);
        cuboidPaint.setStyle(Paint.Style.STROKE);

        // Paint for cube
        Paint cubePaint = new Paint();
        cubePaint.setColor(Color.RED);
        cubePaint.setStrokeWidth(4);
        cubePaint.setStyle(Paint.Style.STROKE);

        // Paint for labels
        Paint textPaint = new Paint();
        textPaint.setColor(Color.BLACK);
        textPaint.setTextSize(40);

        // --- Draw Cuboid ---
        // Front face
        canvas.drawLine(100, 200, 350, 200, cuboidPaint);  // top
        canvas.drawLine(350, 200, 350, 450, cuboidPaint);   // right
        canvas.drawLine(350, 450, 100, 450, cuboidPaint);   // bottom
        canvas.drawLine(100, 450, 100, 200, cuboidPaint);   // left

        // Back face (offset)
        canvas.drawLine(180, 130, 430, 130, cuboidPaint);
        canvas.drawLine(430, 130, 430, 380, cuboidPaint);
        canvas.drawLine(430, 380, 180, 380, cuboidPaint);
        canvas.drawLine(180, 380, 180, 130, cuboidPaint);

        // Connecting edges
        canvas.drawLine(100, 200, 180, 130, cuboidPaint);
        canvas.drawLine(350, 200, 430, 130, cuboidPaint);
        canvas.drawLine(350, 450, 430, 380, cuboidPaint);
        canvas.drawLine(100, 450, 180, 380, cuboidPaint);

        // Label
        canvas.drawText("Cuboid", 170, 520, textPaint);

        // --- Draw Cube ---
        int side = 200;
        int offsetX = 60, offsetY = 60;
        int startX = 550, startY = 200;

        // Front face
        canvas.drawLine(startX, startY, startX + side, startY, cubePaint);
        canvas.drawLine(startX + side, startY, startX + side, startY + side, cubePaint);
        canvas.drawLine(startX + side, startY + side, startX, startY + side, cubePaint);
        canvas.drawLine(startX, startY + side, startX, startY, cubePaint);

        // Back face
        canvas.drawLine(startX + offsetX, startY - offsetY, startX + side + offsetX, startY - offsetY, cubePaint);
        canvas.drawLine(startX + side + offsetX, startY - offsetY, startX + side + offsetX, startY + side - offsetY, cubePaint);
        canvas.drawLine(startX + side + offsetX, startY + side - offsetY, startX + offsetX, startY + side - offsetY, cubePaint);
        canvas.drawLine(startX + offsetX, startY + side - offsetY, startX + offsetX, startY - offsetY, cubePaint);

        // Connecting edges
        canvas.drawLine(startX, startY, startX + offsetX, startY - offsetY, cubePaint);
        canvas.drawLine(startX + side, startY, startX + side + offsetX, startY - offsetY, cubePaint);
        canvas.drawLine(startX + side, startY + side, startX + side + offsetX, startY + side - offsetY, cubePaint);
        canvas.drawLine(startX, startY + side, startX + offsetX, startY + side - offsetY, cubePaint);

        // Label
        canvas.drawText("Cube", 600, 480, textPaint);

        imageView.setImageBitmap(bitmap);
    }
}
```

---

### Output Screenshot

*(Paste screenshot here)*

---

### Observations

The application correctly rendered both a cube and a cuboid on the 2D screen using drawLine() to connect offset vertices, simulating a 3D appearance. Separate Paint objects with distinct colors (blue for cuboid, red for cube) made it straightforward to differentiate between the two shapes. The drawText() method placed text labels ("Cube" and "Cuboid") at the intended positions beneath each shape. The rendered Bitmap was successfully displayed inside an ImageView, confirming that the bitmap served as an effective in-memory frame buffer for the drawing operations.

---

### Conclusions

This experiment demonstrates that 3D graphical primitives can be effectively represented on a 2D Android screen using fundamental drawing APIs. By working with Bitmap, Canvas, and Paint, we established that a convincing 3D effect can be produced through perspective projection — specifically by drawing offset front and back faces and connecting their corresponding vertices. This validates the capability of Android's 2D drawing toolkit for simulating spatial depth in mobile application graphics.

---

### Questions of Curiosity

**1. What is the role of Bitmap in this program?**
The Bitmap functions as the underlying pixel buffer or frame buffer. While Canvas provides the drawing API (lines, shapes, text), the Bitmap is the actual memory allocation where all pixel data is stored. After Canvas completes the rendering, the Bitmap holds the final rasterised image that is displayed on-screen.

**2. How is the 3D effect achieved in this experiment?**
The 3D effect is produced through perspective projection techniques applied on a 2D plane. Since the display is inherently 2D, a scale factor is computed based on the simulated depth (Z-axis distance) of each point from the viewer:
- **Scaling** — Points that are "further away" are drawn smaller and shifted closer to the vanishing point.
- **Transformation** — 3D coordinates (x, y, z) are mapped to 2D screen coordinates (x', y') using a projection ratio, which creates the visual illusion of depth.

**3. What is the function of ImageView in this program?**
The ImageView acts as the UI bridge between the in-memory drawing and the user's screen.
- Canvas and Bitmap operations occur entirely in memory and produce no visible output on their own.
- By calling imageView.setImageBitmap(bitmap), the rendered data is pushed into the Android View hierarchy, making it visible to the user.

---

### References
1. Android Developers, *Canvas and Drawables*, Google Developers Documentation.
2. Android Developers, *Custom View Components*, Google Developers Documentation.
3. Meier, R., *Professional Android Application Development*, Wrox Publications.
