# Proyecto: Calculadora de Índice de Masa Corporal (IMC) con Interfaz Gráfica

Este proyecto consiste en una aplicación de escritorio desarrollada en Python utilizando la librería **Tkinter**. El programa solicita los datos personales del usuario a través de una ventana limpia e intuitiva, realiza validaciones estrictas en tiempo real para asegurar que la información no esté vacía y sea numéricamente correcta, y finalmente calcula y despliega el IMC en la misma interfaz.

## Cómo funciona el programa
1. **Interfaz de Usuario (GUI):** En lugar de la consola tradicional, el programa despliega una ventana interactiva con campos de texto alineados de forma simétrica para una mejor experiencia visual.
2. **Captura y Validación Avanzada:** Al presionar el botón "Calcular IMC", el sistema evalúa los campos mediante bloques `try-except`. Si detecta un campo vacío o un formato de número incorrecto (como texto en la edad o el peso), detiene el proceso y muestra una ventana emergente de alerta (`messagebox.showerror`) detallando el error.
3. **Cálculo del IMC:** Aplica la fórmula matemática estándar dividiendo el peso entre la estatura al cuadrado únicamente si todos los datos ingresados son válidos.
4. **Despliegue de Resultados:** Muestra de forma ordenada el resumen con el nombre completo, datos capturados y el resultado final formateado a dos decimales dentro de un contenedor dedicado en la misma ventana.

## Reflexiones sobre el Bootcamp
* **Evolución del Aprendizaje:** Pasar del desarrollo en consola a interfaces gráficas (GUI) ha sido un gran paso en el bootcamp. Me permitió entender cómo estructurar el código para que responda a eventos del usuario (como hacer clic en un botón) de forma controlada.
* **Importancia de la Validación:** Diseñar las alertas y excepciones con `messagebox` me ayudó a comprender el desarrollo desde la perspectiva del usuario final, donde el software debe ser robusto y guiar a la persona ante cualquier error sin llegar a romperse o cerrarse inesperadamente.
* **Uso de Herramientas Profesionales:** Compartir este tipo de proyectos independientes a través de herramientas como GitHub es fundamental para consolidar lo aprendido, documentar mi avance y aprender a presentar software de manera profesional y accesible.
