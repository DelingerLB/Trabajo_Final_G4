let currentPage = 1;
const usersPerPage = 10;

document.getElementById('showRegisterForm').addEventListener('click', function () {
    const registerSection = document.getElementById('registerSection');
    if (registerSection.style.display === 'none' || !registerSection.style.display) {
        registerSection.style.display = 'block';
        fetchRoles();
    } else {
        registerSection.style.display = 'none';
    }
});

document.getElementById('registerForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const dni = document.getElementById('dni').value;
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    const response = await fetch('http://localhost:8000/users/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ dni: dni, name: name, email: email, phone: phone, password: password, role: role }),
    });

    const result = await response.json();
    const messageElement = document.getElementById('message');

    if (response.ok) {
        messageElement.textContent = 'Usuario creado exitosamente!';
        messageElement.style.color = 'green';
        fetchUsers();  // Refrescar lista de usuarios
    } else if (response.status === 400) {
        messageElement.textContent = result.detail || 'El usuario ya está registrado.';
        messageElement.style.color = 'red';
    } else {
        messageElement.textContent = result.detail || 'Error al crear el usuario. Por favor intenta nuevamente.';
        messageElement.style.color = 'red';
    }

    setTimeout(() => {
        messageElement.textContent = '';
    }, 5000); // Ocultar mensaje después de 5 segundos
});

document.getElementById('refreshUsers').addEventListener('click', function () {
    currentPage = 1;
    fetchUsers();
});

async function fetchUsers(searchTerm = '') {
    const response = await fetch('http://localhost:8000/users/');
    const data = await response.json();
    const userList = document.getElementById('userList');
    userList.innerHTML = '';

    let usersToDisplay = data.users;
    if (searchTerm) {
        usersToDisplay = usersToDisplay.filter(user =>
            user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
            user.dni.includes(searchTerm) ||
            user.phone.includes(searchTerm)
        );
    }

    const startIndex = (currentPage - 1) * usersPerPage;
    const endIndex = startIndex + usersPerPage;
    const paginatedUsers = usersToDisplay.slice(startIndex, endIndex);

    paginatedUsers.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.dni}</td>
            <td>${user.name}</td>
            <td>${user.email}</td>
            <td>${user.phone}</td>
            <td>${user.role}</td>
            <td><button onclick="deleteUser(${user.id})">Eliminar</button></td>
        `;
        userList.appendChild(row);
    });

    if (endIndex >= usersToDisplay.length) {
        document.getElementById('refreshUsers').style.display = 'none';
    } else {
        document.getElementById('refreshUsers').style.display = 'block';
    }
}

// Fetch users when the page loads
fetchUsers();

document.getElementById('searchInput').addEventListener('input', function (event) {
    const searchTerm = event.target.value;
    fetchUsers(searchTerm);
});

// Función para obtener y mostrar roles disponibles
async function fetchRoles() {
    const response = await fetch('http://localhost:8001/roles/');
    const data = await response.json();
    const roleSelect = document.getElementById('role');
    roleSelect.innerHTML = '';

    data.forEach(role => {
        const option = document.createElement('option');
        option.value = role.name;
        option.textContent = role.name;
        roleSelect.appendChild(option);
    });
}

// Función para eliminar un usuario
async function deleteUser(userId) {
    const response = await fetch(`http://localhost:8000/users/${userId}`, {
        method: 'DELETE',
    });

    const result = await response.json();
    if (response.ok) {
        alert(result.message);
        fetchUsers();
    } else {
        alert(result.detail || 'Error al eliminar el usuario. Por favor intenta nuevamente.');
    }
}
