document.addEventListener("DOMContentLoaded", function () {
    loadAccounts(); // Load accounts on page load

    document.querySelector(".panel-group form").addEventListener("submit", function (event) {
        event.preventDefault();
        addAccount();
    });

    document.querySelector(".table tbody").addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-btn")) {
            deleteAccount(event.target.dataset.email);
        }
    });
});

// Function to add a new account
function addAccount() {
    let email = document.querySelector("input[type='email']").value;
    let username = document.querySelector("input[type='text']").value;
    let password = document.querySelector("input[type='password']").value;

    if (!email || !username || !password) {
        alert("Please fill in all fields!");
        return;
    }

    let accounts = JSON.parse(localStorage.getItem("accounts")) || [];
    
    // Check if account already exists
    if (accounts.some(acc => acc.email === email)) {
        alert("Account with this email already exists!");
        return;
    }

    let newAccount = { email, username };
    accounts.push(newAccount);
    localStorage.setItem("accounts", JSON.stringify(accounts));

    loadAccounts(); // Refresh table
    document.querySelector(".panel-group form").reset(); // Clear form
}

// Function to load accounts from LocalStorage
function loadAccounts() {
    let accounts = JSON.parse(localStorage.getItem("accounts")) || [];
    let tableBody = document.querySelector(".table tbody");
    tableBody.innerHTML = ""; // Clear existing rows

    accounts.forEach((account, index) => {
        let row = `<tr>
            <td>${index + 1}</td>
            <td>${account.username}</td>
            <td>${account.email}</td>
            <td>
                <a href="#" class="delete-btn" data-email="${account.email}">
                    <i class="fa fa-trash-o"></i>
                </a>
            </td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

// Function to delete an account
function deleteAccount(email) {
    let accounts = JSON.parse(localStorage.getItem("accounts")) || [];
    accounts = accounts.filter(acc => acc.email !== email);
    localStorage.setItem("accounts", JSON.stringify(accounts));

    loadAccounts(); // Refresh table
}
