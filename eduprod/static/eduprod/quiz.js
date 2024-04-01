document.addEventListener("DOMContentLoaded", function() {
    let currentFlashcardIndex = 0;
    const flashcards = JSON.parse(document.getElementById('flashcard-container').getAttribute('data-flashcards'));
    const flashcardContainer = document.getElementById('flashcard-container');
    const revealBtn = document.getElementById('revealBtn');

    function displayFlashcard() {
        if (currentFlashcardIndex < flashcards.length) {
            const front = flashcards[currentFlashcardIndex].fields.front;
            const back = flashcards[currentFlashcardIndex].fields.back;
            flashcardContainer.innerHTML = `<div class='flashcard'><p class='front'>Front: ${front}</p><p class='back' style='display: none;'>Back: ${back}</p></div>`;
            revealBtn.textContent = "Reveal Answer";
        } else {
            flashcardContainer.innerHTML = "No more flashcards.";
            revealBtn.style.display = "none";
        }
    }

    displayFlashcard();

    revealBtn.addEventListener("click", function() {
        const backElement = flashcardContainer.querySelector('.back');
        if (revealBtn.textContent === "Reveal Answer") {
            backElement.style.display = "block";
            revealBtn.textContent = "Next Flashcard";
        } else {
            currentFlashcardIndex++;
            displayFlashcard();
        }
    });
});
