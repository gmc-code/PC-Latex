====================================================
RayTracing
====================================================


| For checking the curvature of mirrors, use a circle with center at twice the focal length.
| For lenses, use a circle at the focal length for a close approximation.
----

Lensmaker's Equation
====================

The focal length \( f \) of a thin lens in air is given by:

.. math::

   \frac{1}{f} = (n - 1) \left( \frac{1}{R_1} - \frac{1}{R_2} \right)

Where:

- \( f \) is the focal length of the lens
- \( n \) is the refractive index of the lens material
- \( R_1 \) is the radius of curvature of the first lens surface
- \( R_2 \) is the radius of curvature of the second lens surface

For a symmetric lens where \( R_1 = -R_2 = R \), the equation simplifies to:

.. math::

   \frac{1}{f} = \frac{2(n - 1)}{R}

Solving for \( R \):

.. math::

   R = 2(n - 1)f

| For acrylic, n = 1.49.
| So R = 0.98 f
| Hence, a circle of radius, f, at f, will be clos enough to manually observe curvature.

----

Optical axes
-------------------

| A simple cross shape on the landscape page is useful for ray diagrams.

.. figure:: files/optical_axes.png
   :width: 300
   :alt: optical_axes.png
   :figclass: align-center


.. literalinclude:: files/optical_axes_2pages.tex
   :linenos:

| Downloads
| :download:`optical_axes_2pages.pdf<files/optical_axes_2pages.pdf>`
| :download:`optical_axes_2pages.tex<files/optical_axes_2pages.tex>`

----

Biconcave lens
-------------------

| Student version and full versions are shown below.

.. figure:: files/biconcave_lens.png
   :width: 300
   :alt: biconcave_lens.png
   :figclass: align-center


.. literalinclude:: files/biconcave_lens.tex
   :linenos:

| Downloads
| :download:`biconcave_lens.pdf<files/biconcave_lens.pdf>`
| :download:`biconcave_lens.tex<files/biconcave_lens.tex>`

.. figure:: files/biconcave_lens_student.png
   :width: 300
   :alt: biconcave_lens_student.png
   :figclass: align-center


.. literalinclude:: files/biconcave_lens_student.tex
   :linenos:

| Downloads
| :download:`biconcave_lens_student.pdf<files/biconcave_lens_student.pdf>`
| :download:`biconcave_lens_student.tex<files/biconcave_lens_student.tex>`


----

Biconvex lens
-------------------

| Student version and full versions are shown below.

.. figure:: files/biconvex_lens.png
   :width: 300
   :alt: biconvex_lens.png
   :figclass: align-center


.. literalinclude:: files/biconvex_lens.tex
   :linenos:

| Downloads
| :download:`biconvex_lens.pdf<files/biconvex_lens.pdf>`
| :download:`biconvex_lens.tex<files/biconvex_lens.tex>`

.. figure:: files/biconvex_lens_student.png
   :width: 300
   :alt: biconvex_lens_student.png
   :figclass: align-center


.. literalinclude:: files/biconvex_lens_student.tex
   :linenos:

| Downloads
| :download:`biconvex_lens_student.pdf<files/biconvex_lens_student.pdf>`
| :download:`biconvex_lens_student.tex<files/biconvex_lens_student.tex>`
