// document.addEventListener("htmx:confirm", function (e) {
//    // action based on user response
//    url = $(this).attr('href')
//    if (confirm(`${e.detail.question}`)) {
//       e.detail.issueRequest(true);
//    } else {
//       window.location = $(this).attr('href')
//    }
// });

// document.getElementById("btn-delete").addEventListener("click", function () {
//    // invoke the function
//    let userChoice = confirm("Do you want to delete this file?");
//    // action based on user response
//    if (userChoice) {
//       alert("File deleted!");
//    } else {
//       alert("Deletion cancelled.");
//    }
// });

// $('.delete').click(function (e) {
//     e.preventDefault()
//     url = $(this).attr('href')
//     if (confirm('Are you sure you want to delete?'))
//         return;
//     window.location = $(this).attr('href')
// });

// function confirmDelete() {
//     e.preventDefault()
//     url = $(this).attr('href')
//     if (!confirm('Are you sure you want to delete?'))
//         return;
//     window.location = $(this).attr('href');
// };

// document.addEventListener("htmx:confirm", function (e) {
//     e.preventDefault()
//     Swal.fire({
//         title: "Please confirm action",
//         text: `${e.detail.question}`
//     }).then(function (result) {
//         if (result.isConfirmed) e.detail.issueRequest(true) // use true to skip window.confirm
//     })
// })
