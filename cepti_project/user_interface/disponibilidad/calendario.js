document.addEventListener('DOMContentLoaded', function () {
    const terapeutasList = document.getElementById('terapeutas-list');
    const calendarContainer = document.getElementById('calendar-container');
    const terapeutaName = document.getElementById('terapeuta-name');
    const calendarBody = document.getElementById('calendar-body');

    async function fetchTerapeutas() {
        const response = await fetch('http://localhost:8000/terapeutas/');
        const terapeutas = await response.json();

        terapeutasList.innerHTML = '';

        terapeutas.forEach(terapeuta => {
            const row = document.createElement('tr');
            row.classList.add('terapeuta-row');
            row.innerHTML = `<td>${terapeuta.name}</td><td>${terapeuta.specialty}</td>`;
            row.addEventListener('click', () => showCalendar(terapeuta));
            terapeutasList.appendChild(row);
        });
    }

    async function fetchDisponibilidad(terapeuta_id) {
        const response = await fetch(`http://localhost:8000/disponibilidad/?terapeuta_id=${terapeuta_id}`);
        const disponibilidad = await response.json();
        return disponibilidad;
    }

    function buildCalendar(disponibilidad) {
        calendarBody.innerHTML = '';

        const hours = ['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'];
        const days = ['Lunes', 'Martes', 'Miércoles', 'Jueves'];

        hours.forEach(hour => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${hour}</td>`;

            days.forEach((day, index) => {
                const cell = document.createElement('td');
                cell.classList.add('calendar-cell');
                cell.addEventListener('click', () => toggleReservation(cell));
                row.appendChild(cell);
            });

            calendarBody.appendChild(row);
        });

        // Marcar casillas ocupadas
        disponibilidad.forEach(d => {
            const date = new Date(d.fecha);
            const day = date.getDay() - 1;  // Lunes=0, Martes=1, etc. (0-based index)
            const hour = `${d.hora_inicio.split(':')[0]}:00`;

            const row = [...calendarBody.querySelectorAll('tr')].find(r => r.cells[0].innerText === hour);
            if (row && day >= 0 && day < 4) {
                const cell = row.cells[day + 1];
                cell.classList.add('reserved');
                cell.textContent = 'Ocupado';
            }
        });
    }

    function toggleReservation(cell) {
        if (cell.textContent === 'Ocupado') {
            return;  // No permitir desmarcar las casillas ocupadas
        }

        if (cell.classList.contains('reserved')) {
            cell.classList.remove('reserved');
            cell.textContent = '';
        } else {
            cell.classList.add('reserved');
            cell.textContent = 'Reservado';
        }
    }

    async function showCalendar(terapeuta) {
        terapeutaName.textContent = `Disponibilidad de ${terapeuta.name}`;
        calendarContainer.style.display = 'block';
        const disponibilidad = await fetchDisponibilidad(terapeuta.id);
        buildCalendar(disponibilidad);
    }

    fetchTerapeutas();
});
