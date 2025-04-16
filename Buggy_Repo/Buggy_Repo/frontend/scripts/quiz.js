const BASE_URL = "http://localhost:8000";

let score = 0;
let highScore = 0;
let currentQuestion = null;
let gameOver = false;
let attemptHistory = [];

// DOM elements
const scoreDisplay = document.getElementById("scoreDisplay");
const questionDiv = document.getElementById("question");
const form = document.getElementById("answerForm");
const feedback = document.getElementById("feedback");
const resetBtn = document.getElementById("resetBtn");
const attemptList = document.getElementById("attemptList");
const attemptCount = document.getElementById("attemptCount");
const searchInput = document.getElementById("search");

// Updates the score display
function updateScoreDisplay() {
  scoreDisplay.textContent = `Score: ${score} | High Score: ${highScore}`;
}

// Updates the attempts list and applies search filter
function updateAttempts() {
  const search = searchInput.value.toLowerCase();
  const filtered = attemptHistory.filter(a =>
    a.question.toLowerCase().includes(search) // Search attempts by question text
  );

  // Generate the list of attempts
  attemptList.innerHTML = filtered.map(a => `
    <div>
      <strong>${a.question}</strong><br/>
      Your answer: ${a.answer} — ${a.result}
    </div>
  `).join("");

  // Update the attempt count
  attemptCount.textContent = `Total attempts: ${filtered.length}`;
}

// Attach event listener for filtering attempts based on search input
searchInput.addEventListener("input", updateAttempts);

// Load the high score from the backend
async function loadHighScore() {
  try {
    const res = await fetch(`${BASE_URL}/quiz/highscore`);
    const data = await res.json();
    highScore = data.high_score;
    updateScoreDisplay();
  } catch {
    feedback.textContent = "Failed to load high score."; // Handle fetch error
  }
}

// Load the next question from the backend
async function loadQuestion() {
  if (gameOver) return; // If the game is over, don't load a new question

  try {
    const res = await fetch(`${BASE_URL}/quiz/question`);
    const data = await res.json();
    currentQuestion = data;

    // Display the question text
    questionDiv.textContent = data.text;

    // Display the options dynamically
    form.innerHTML = data.options.map(option => `
      <label>
        <input type="radio" name="answer" value="${option}" required>
        ${option}
      </label><br/>
    `).join("") + `<button type="submit">Submit</button>`;

    // Attach the question ID to the form for later use
    form.dataset.id = data.id;
    feedback.textContent = "";
  } catch {
    feedback.textContent = "Failed to load question."; // Handle fetch error
  }
}

// Event listener for answer submission
form.addEventListener("submit", async (e) => {
  e.preventDefault(); // Prevent default form submission
  if (gameOver) return; // If the game is over, don't process the answer

  const selected = form.querySelector("input[name=answer]:checked");
  if (!selected) return; // If no option is selected, don't submit

  const answer = selected.value;
  const id = parseInt(form.dataset.id); // Get the current question ID

  try {
    const res = await fetch(`${BASE_URL}/quiz/answer`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id, answer, score }) // Send the current answer and score to the backend
    });

    const data = await res.json();

    if (data.error) {
      feedback.textContent = data.error; // Handle invalid response or error from backend
      return;
    }

    // Add the attempt to the history
    attemptHistory.push({
      question: currentQuestion.text,
      answer,
      result: data.is_correct ? "✅ Correct" : `❌ Wrong (Correct: ${data.correct_answer})`
    });

    updateAttempts(); // Update the attempts list

    if (data.is_correct) {
      score = data.score;
      highScore = data.high_score;
      updateScoreDisplay(); // Update score and high score
      feedback.textContent = "✅ Correct!";
      await loadQuestion(); // Load the next question
    } else {
      feedback.textContent = `❌ Incorrect. Correct answer: ${data.correct_answer}. Game Over.`;
      gameOver = true; // End the game if the answer is incorrect
      form.innerHTML = ""; // Clear the form
      resetBtn.classList.remove("hidden"); // Show reset button
    }
  } catch {
    feedback.textContent = "Error submitting answer."; // Handle any error during submission
  }
});

// Event listener for reset button click
resetBtn.addEventListener("click", () => {
  score = 0;
  gameOver = false;
  attemptHistory = []; // Reset attempt history
  updateScoreDisplay();
  updateAttempts();
  resetBtn.classList.add("hidden");
  loadQuestion(); // Load the next question after reset
});

// Initialize the game on page load
window.addEventListener("DOMContentLoaded", async () => {
  await loadHighScore(); // Load the high score first
  loadQuestion(); // Load the first question
});
