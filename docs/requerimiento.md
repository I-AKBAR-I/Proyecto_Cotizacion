# Requerimientos

## Requerimientos Funcionales

### Registro de Entidades
1. **Ventanas:**
   - Registro de estilos: O, XO, OXXO, OXO (otros estilos requieren autorización).
   - Atributos: tipo de ventana, dimensiones (ancho y alto), y número de naves.
   
2. **Naves:**
   - Tipos: O o X.
   - Atributos: dimensiones (ancho y alto), tipo de vidrio (transparente, bronce, azul), acabado de aluminio (pulido, lacado brillante, lacado mate, anodizado), opción de esmerilado.

3. **Vidrio:**
   - Atributos: tipo (transparente, bronce, azul), precio por cm².

4. **Acabado de Aluminio:**
   - Atributos: tipo de acabado y precio por metro lineal.

5. **Elementos Adicionales:**
   - Esquinas ($4,310 por unidad), chapas ($16,200 por unidad para naves X), y materiales incluidos como remaches, tornillos, caucho.

6. **Clientes:**
   - Atributos: nombre, tipo de cliente (empresa constructora), dirección de contacto.

7. **Cotizaciones:**
   - Atributos: fecha, número de cotización, cliente, lista de ventanas, y descuento si corresponde.

### Cálculo de Precios
1. **Cálculo del costo de ventanas:**
   - Basado en las dimensiones y estilo de la ventana.
   - Cálculo del tamaño de cada nave y ajuste del vidrio (1.5 cm menos por cada lado).
   - Precio de aluminio por metro lineal, según acabado.
   - Precio del vidrio por cm², con costo adicional por esmerilado.
   - Precio de esquinas y chapas (si aplica).

2. **Descuentos:**
   - Aplicar 10% de descuento si se superan las 100 ventanas del mismo diseño.

### Gestión de Relaciones
1. Asociar varios estilos de ventanas a un cliente.
2. Relacionar naves con ventanas y ajustar las dimensiones de las naves.
3. Asignar tipo de vidrio y acabado de aluminio a cada nave.
4. Calcular automáticamente el número de esquinas y chapas necesarias por ventana.

### Consultas y Reportes
1. Consultar detalles de ventanas (tipo, dimensiones, naves, vidrio, acabado, costo total).
2. Consultar información de clientes (nombre, tipo de cliente, cotizaciones solicitadas).
3. Consultar cotizaciones realizadas (cliente, fecha, costo total).
4. Generar informes de cotización con desglose de costos y aplicación de descuentos.

### Validaciones
1. Verificar que las dimensiones de las naves sean coherentes con el tamaño de la ventana.
2. Asegurar que el vidrio sea 1.5 cm más pequeño que la nave en cada lado.
3. Validar que el descuento solo se aplique a más de 100 ventanas del mismo diseño.

---

## Requerimientos No Funcionales

1. **Interfaz de Usuario:**
   - Simple y orientada a empresas.
   - Debe permitir ingresar las dimensiones, estilo, tipo de vidrio, y acabado de aluminio.

2. **Base de Datos:**
   - Almacenar precios y especificaciones de todos los materiales, vidrios, acabados, chapas, etc.

3. **Mantenibilidad:**
   - Fácil actualización de precios y estilos de ventanas.

4. **Escalabilidad:**
   - Capacidad para manejar grandes pedidos, como los de constructoras.
