document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registerForm');
    const message = document.getElementById('message');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = {
            nombrePaciente: document.getElementById('nombrePaciente').value,
            apellidoPaciente: document.getElementById('apellidoPaciente').value,
            dniPaciente: document.getElementById('dniPaciente').value,
            fechaNacimiento: document.getElementById('fechaNacimiento').value,
            nombreApoderado: document.getElementById('nombreApoderado').value,
            apellidoApoderado: document.getElementById('apellidoApoderado').value,
            dniApoderado: document.getElementById('dniApoderado').value,
            telefonoApoderado: document.getElementById('telefonoApoderado').value,
            direccion: document.getElementById('direccion').value
        };

        // Validaciones básicas
        if (!formData.nombrePaciente || !formData.apellidoPaciente || !formData.dniPaciente ||
            !formData.fechaNacimiento || !formData.nombreApoderado || !formData.apellidoApoderado ||
            !formData.dniApoderado || !formData.telefonoApoderado || !formData.direccion) {
            message.textContent = 'Por favor, completa todos los campos';
            message.style.color = 'red';
            return;
        }

        // Enviar datos al backend
        const response = await fetch('http://localhost:8000/paciente/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            message.textContent = 'Registro exitoso';
            message.style.color = 'green';
            form.reset();
        } else {
            const result = await response.json();
            message.textContent = result.detail || 'Error al registrar. Inténtalo de nuevo.';
            message.style.color = 'red';
        }
    });
});
