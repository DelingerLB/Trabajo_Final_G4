document.addEventListener('DOMContentLoaded', function () {
    const planesList = document.getElementById('planes-list');

    async function fetchPlanes() {
        const response = await fetch('http://localhost:8000/planes/');
        const planes = await response.json();
        planesList.innerHTML = '';

        planes.forEach(plan => {
            const planElement = document.createElement('div');
            planElement.textContent = `Plan ID: ${plan.id}`;
            planesList.appendChild(planElement);
        });
    }

    document.getElementById('confirm-button').addEventListener('click', async function () {
        const response = await fetch('http://localhost:8000/planes/generar/', {
            method: 'POST',
        });

        if (response.ok) {
            fetchPlanes();
            alert('Planes confirmados exitosamente!');
        } else {
            alert('Error al confirmar los planes. Por favor intenta nuevamente.');
        }
    });

    fetchPlanes();
});
