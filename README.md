# Python Test :metal: :zap:

## Contexto

La empresa Ilusiones S.A. de C.V. vende equipos celulares y necesita realizar compras de mercancía a través de 2 archivos que envía la empresa matriz y que corresponden a 2 archivos:
un archivo Excel de Orden de Compras y otro archivo Excel de Recepción de Mercancía.

> Consideraciones del archivo de Orden de Compras:

1. Cada fila es una orden de compra para 1 solo almacén. Solo debe existir 1 solo almacén por archivo, es decir no se debe repetir en otra fila.
2. La columna A (Sub inventario) es un identificador único del almacén.
3. La columna B (PDV) es el nombre del almacén.
4. La columna C-EJ es el SKU único por modelo de equipo celular y en cada celda se especifica la cantidad de equipos requeridos para cada almacén.
5. La columna EK (Total) es el total de mercancía por almacén.

> Consideraciones del archivo de Recepción de Mercancía:

1. Cada equipo celular que llega está representado en cada fila.
2. La columna A (Sub inventario) es un identificador único del almacén.
3. La columna B (Nombre) es el nombre del almacén.
4. La columna C (Modelo) representa el SKU único por modelo de los equipos celulares.
5. La columna D (IMEI) es el identificador único del equipo celular.
6. La columna D (Folio) es el Folio de la entrega de la mercancía.

## Objetivo del Ejercicio

Desarrollar un API REST y las interfaces que la consuman para realizar el flujo de compras de mercancía para la empresa Ilusiones S.A. de C.V. generando las ordenes de compras para cada
almacén de acuerdo al archivo Orden de Compras y realizando la recepción de la mercancía para cada almacén de acuerdo al archivo Recepción de Mercancía.
Todo esto en un plazo no mayor a 48 horas.

## Objetivos específicos

* Establecer los tipos de datos para los campos de acuerdo a la información de los 2 archivos
* Módulo CRUD de Almacenes
    + Crear los almacenes necesarios para la orden y recepción de la mercancía
    + Agregar campo Sub inventario por cada almacén=> Único por almacén
    + Validar campos
* Módulo CRUD de Órdenes de Compra
    + Agregar sección para importar archivo de Orden de Compra
    + Leer el archivo Orden de Compra y crear las órdenes de compra por cada almacén con un estatus listo para recepción de mercancía
    + Validar que el archivo cumpla con las columnas necesarias para su lectura, de lo contrario lanzar un error
    + Validar al cargar el archivo si el almacén existe a través del código de subinventario, de lo contrario lanzar un error
    + Recepción de Mercancia:
        - Agregar una sección en el detalle de cada orden de compra para importar el archivo de Recepción de Mercancía
        - Leer el archivo de Recepción de Mercancía y agregar al inventario de cada almacén los productos recibidos
        - Validar que el archivo cumpla con las columnas necesarias para su lectura, de lo contrario lanzar un error
        - Validar al cargar el archivo si el almacén existe a través del código de subinventario, de lo contrario lanzar un error
        - Validar que el IMEI del producto sea único en el inventario, de lo contrario lanzar un error.
* Módulo CRUD para Productos
    + Por cada SKU que se encuentre en el archivo Orden de Compra, revisar si existe en el catálogo de productos, de lo contrario agregar en el catálogo el equipo celular de forma automática.
    + En caso de que sea un producto nuevo agregar campo SKU único por modelo para validar posteriormente
    + Validar campos
* Modulo Inventario
    + Mostrar el inventario actual por Almacén
        - Agregar Filtros
