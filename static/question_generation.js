document.addEventListener("DOMContentLoaded", function () {
    // Add your JavaScript code for handling client-side interactions here
    // For example, you can use AJAX to make requests to your Flask server.

    // When the "Generate Questions" button is clicked:
    document.getElementById("generate-questions-button").addEventListener("click", function () {
        // Get the context and question type from the user input
        const context = document.getElementById("context-input").value;
        const questionType = document.getElementById("question-type-select").value;

        // Make an AJAX request to the Flask server
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/generate_questions", true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.onload = function () {
            if (xhr.status === 200) {
                // Display the generated questions on the page
                const questions = JSON.parse(xhr.responseText);
                const questionsList = document.getElementById("questions-list");
                questionsList.innerHTML = "";
                questions.forEach(function (question, index) {
                    const listItem = document.createElement("li");
                    listItem.innerHTML = question;
                    questionsList.appendChild(listItem);
                });
            }
        };

        // Send the context and question type as JSON data
        const data = JSON.stringify({ context: context, question_type: questionType });
        xhr.send(data);
    });
});
