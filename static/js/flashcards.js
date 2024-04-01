const flashcards = {{ flashcards|safe }};
let currentCardIndex = 0;

function revealAnswer() {
    const answer = document.querySelector('.flashcard .answer');
    answer.style.display = 'block';
}

function showNextCard() {
    currentCardIndex++;
    if (currentCardIndex >= flashcards.length) {
        currentCardIndex = 0;
    }
    const currentFlashcard = flashcards[currentCardIndex];
    const flashcardContainer = document.getElementById('flashcard-container');
    flashcardContainer.innerHTML = `
        <div class="flashcard">
            <p class="question">${currentFlashcard.front}</p>
            <p class="answer" style="display: none;">${currentFlashcard.back}</p>
        </div>
    `;
    // Update the flashcard ID in the form
    document.querySelector('#save-form input[name="flashcard_id"]').value = currentFlashcard.id;
}