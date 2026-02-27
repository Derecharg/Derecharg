---
name: "Selling Study Materials for Law Students (Derecharg)"
description: "Configures the 'Comprar Apuntes' buttons in index.html, uses the user's CBU or MercadoPago link, and creates a simple and professional gracias.html that displays 'En breve recibirás el material en tu correo' after a purchase."
---

# Selling Study Materials for Law Students (Derecharg)

This skill configures the landing page of Derecharg to sell study materials for law students at UNLP.

## Steps

1. **Review `index.html`**:
   - Analyze the `index.html` file to locate the existing payment buttons ("Pagar con Mercado Pago" and "Transferencia Bancaria").
   - Ensure the buttons have the correct text, links, and styling.
   
2. **Configure 'Comprar Apuntes' Buttons**:
   - For Mercado Pago: Ensure the link points to the user's current MercadoPago link (e.g., `https://mpago.la/1CubSAX`).
   - For Transfer: Ensure the modal displays the user's CBU/Alias and instructions clearly.
   - Update the button text to "Comprar Apuntes" if requested, or keep the existing clear calls to action ("Pagar con Mercado Pago" / "Transferencia Bancaria").
   
3. **Create `gracias.html`**:
   - Create a new file named `gracias.html` in the same directory as `index.html`.
   - Build a simple, professional, and responsive page using the project's existing CSS (`style.css`).
   - Include the Derecharg logo and branding colors (Deep Blue `#003366`, Gold `#e6b400`).
   - The central message must be: **"En breve recibirás el material en tu correo"**.
   - Add a button to return to the main landing page (`index.html`).
   
4. **Link Successful Payments to `gracias.html` (Optional/Future)**:
   - If using a direct MercadoPago link, instruct the user on how to configure the `back_urls` in their MercadoPago dashboard to redirect to `gracias.html` upon successful payment.
   - For manual transfers, the user is currently directed to WhatsApp to send the receipt.

## Usage

To execute this skill, the agent should:
1. Read `index.html` to find the payment buttons.
2. Modify `index.html` to ensure the buttons are configured correctly.
3. Use `write_to_file` to create `gracias.html` with the required design and message.
4. Notify the user that the setup is complete and provide instructions on how to test it.
