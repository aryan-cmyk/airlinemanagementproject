document.addEventListener("DOMContentLoaded", function () {
  const crewForm = document.getElementById("crewForm");

  if (crewForm) {
    crewForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const newCrew = {
        name: document.getElementById("crewName").value,
        crew_id: document.getElementById("crewId").value,
        role: document.getElementById("crewRole").value,
        available_days: document.getElementById("availableDays").value,
        experience: document.getElementById("experience").value,
      };

      let crews = JSON.parse(localStorage.getItem("crews")) || [];
      crews.push(newCrew);
      localStorage.setItem("crews", JSON.stringify(crews));
      alert("Crew member added successfully!");
      crewForm.reset();
    });
  }

  // Populate dropdown
  const crewDropdown = document.getElementById("assignCrewId");
if (crewDropdown) {
  const crews = JSON.parse(localStorage.getItem("crews")) || [];
  crews.forEach((c) => {
    let opt = document.createElement("option");
    opt.value = c.crew_id;
    opt.text = `${c.crew_id} - ${c.name}`;
    crewDropdown.appendChild(opt);
  });
}

  // Assign crew
  const assignForm = document.getElementById("assignForm");
  if (assignForm) {
    assignForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const assignment = {
        crew_id: document.getElementById("assignCrewId").value,
        flight_no: document.getElementById("flight_no").value,
        date: document.getElementById("assign_date").value,
      };

      let assignments = JSON.parse(localStorage.getItem("assignments")) || [];

      const exists = assignments.some(
        (a) => a.crew_id === assignment.crew_id && a.date === assignment.date
      );

      if (exists) {
        alert("Crew already assigned on this date.");
        return;
      }

      assignments.push(assignment);
      localStorage.setItem("assignments", JSON.stringify(assignments));
      alert("Crew assigned successfully!");
      assignForm.reset();
    });
  }

  // View schedule
  const scheduleInput = document.getElementById("schedule_date");
  if (scheduleInput) {
    scheduleInput.addEventListener("change", function () {
      const selectedDate = this.value;
      const crews = JSON.parse(localStorage.getItem("crews")) || [];
      const assignments = JSON.parse(localStorage.getItem("assignments")) || [];
      const table = document.getElementById("scheduleTable");
      table.innerHTML = "";

      const results = assignments
        .filter((a) => a.date === selectedDate)
        .map((a) => {
          const crew = crews.find((c) => c.crew_id === a.crew_id);
          return `<tr>
              <td>${crew.crew_id}</td>
              <td>${crew.name}</td>
              <td>${crew.role}</td>
              <td>${a.flight_no}</td>
            </tr>`;
        });

      table.innerHTML = results.length
        ? results.join("")
        : `<tr><td colspan="4">No assignments</td></tr>`;
    });
  }
});
