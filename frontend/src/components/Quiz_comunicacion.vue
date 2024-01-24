<template>
  <div class="flex center">
    <div class="wrapper">
      <div class="quiz-container">
        <div class="quiz-head">
          <h1 class="quiz-title">Quizz</h1>
          <div class="quiz-score flex">
            <span>{{ correctScore }}</span
            >/<span>{{ totalQuestion }}</span>
          </div>
        </div>
        <div class="quiz-body">
          <h2 class="quiz-question">
            {{ question }}
            <span class="category">{{ category }}</span>
          </h2>
          <ul class="quiz-options">
            <li
              v-for="(option, index) in options"
              :key="index"
              @click="selectOption(index)"
              :class="{ selected: selectedOptionIndex === index }"
            >
              {{ option }}
            </li>
          </ul>
          <div id="result" v-html="formattedResultMessage"></div>
        </div>
        <div class="quiz-foot">
          <button
            @click="checkAnswer"
            :disabled="disableCheckButton"
            v-if="!showPlayAgainBtn"
          >
            Confirmar respuesta
          </button>
          <span style="margin: 0 10px"></span>
          <!-- Este es el margen -->
          <button @click="restartQuiz" v-if="showPlayAgainBtn">
            Jugar de nuevo
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
:root {
  --light-purple-color: #8854c0;
  --light-color: #fff;
  --dark-color: #000;
  --grey-color: #f2f2f2;
  --transition: all 300ms ease-in-out;
}
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}
body {
  min-height: 100vh;
  font-family: "Poppins", sans-serif;
  color: var(--dark-color);
  background: var(--grey-color);
}
.wrapper {
  background: var(--light-color);
  padding: 1.5rem 4rem 3rem 4rem;
  width: 600px;
  height: 680px;
  border-top-left-radius: 1.5rem;
  border-bottom-right-radius: 1.5rem;
  position: relative;
  box-shadow: 0 4px 6px rgb(0 0 0 / 10%), 0 1px 3px rgb(0 0 0 / 10%);
}
.quiz-title {
  text-align: center;
  font-size: 2rem;
}
.quiz-score {
  text-align: right;
  font-weight: 600;
  font-size: 1.2rem;
  margin-bottom: 1rem;
  border: 5px solid var(--grey-color);
  font-weight: bold;
  width: 100px;
  height: 50px;
  margin: 0.5rem auto 1rem auto;
  color: var(--light-purple-color);
}
.quiz-question {
  font-size: 1.2rem;
  text-align: center;
  line-height: 1.3;
  margin-bottom: 2rem;
}
.quiz-question .category {
  font-size: 0.9rem;
  font-weight: 500;
  background-color: var(--light-purple-color);
  color: var(--light-color);
  padding: 0.2rem 0.4rem;
  border-radius: 0.2rem;
  margin-top: 0.5rem;
  display: inline-block;
}
.quiz-options {
  list-style-type: none;
  margin: 1rem 0;
}
.quiz-options li {
  border-radius: 0.5rem;
  font-weight: 600;
  margin: 0.7rem 0;
  padding: 0.4rem 1.2rem;
  cursor: pointer;
  border: 3px solid var(--light-purple-color);
  background-color: var(--light-purple-color);
  color: var(--light-color);
  box-shadow: 0 4px 0 0 #6c4298;
  transition: var(--transition);
}
.quiz-options li:hover {
  background-color: var(--grey-color);
  color: var(--dark-color);
  border-color: var(--grey-color);
  box-shadow: 0 4px 0 0 #bbbbbb;
}
.quiz-options li:active {
  transform: scale(0.97);
}
/* js related */
.selected {
  background-color: var(--grey-color) !important;
  color: var(--dark-color) !important;
  border-color: var(--grey-color) !important;
  box-shadow: 0 4px 0 0 #bbbbbb !important;
}
.quiz-foot button {
  border: none;
  border-radius: 0.5rem;
  outline: 0;
  font-family: "Poppins", sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  padding: 0.5rem 1rem;
  margin: 0 auto 0 auto;
  text-transform: uppercase;
  cursor: pointer;
  display: block;
  background-color: var(--grey-color);
  color: var(--dark-color);
  letter-spacing: 2px;
  transition: var(--transition);
  box-shadow: 0 4px 0 0 #bbbbbb;
}
.quiz-foot button:hover {
  background-color: #e6e6e6;
  box-shadow: 0 4px 0 0 #a7a7a7;
}
.quiz-foot button:active {
  transform: scale(0.95);
}
#play-again {
  display: none;
}
#result {
  padding: 0.7rem 0;
  text-align: center;
  font-weight: 600;
  font-size: 1.3rem;
}
#result i {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  line-height: 30px;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
  background-color: var(--light-purple-color);
  color: var(--light-color);
}

@media (max-width: 678px) {
  .quiz-title {
    font-size: 1.6rem;
  }
  .wrapper {
    margin: 3rem 0;
    width: 90%;
    height: 90%;
    padding: 1.5rem 1rem 3rem 1rem;
    border-top-left-radius: 0;
    border-bottom-right-radius: 0;
  }
  .quiz-foot button {
    font-size: 1rem;
  }
}
</style>

<script>
export default {
  data() {
    return {
      question: "",
      category: "",
      options: [],
      correctAnswer: "",
      correctScore: 0,
      totalQuestion: 10,
      askedCount: 0,
      resultMessage: "",
      selectedOptionIndex: null,
      currentQuestionNumber: 1,
      disableCheckButton: false,
    };
  },
  computed: {
    formattedResultMessage() {
      if (!this.resultMessage) return ""; // Evitar errores si resultMessage es nulo o indefinido

      return this.resultMessage
        .replace(/'/g, '"') // Reemplazar comillas simples con comillas dobles
        .replace(/\${this.correctAnswer}/g, this.correctAnswer);
    },
    checkBtnDisabled() {
      return this.selectedOptionIndex === null;
    },
    showPlayAgainBtn() {
      return this.askedCount === this.totalQuestion;
    },
  },
  mounted() {
    this.loadQuestion();
  },
  methods: {
    async loadQuestion() {
      const APIUrl = `http://54.89.201.63:5000/quiz-comunicacion/${this.currentQuestionNumber}`;
      const result = await fetch(APIUrl);
      const data = await result.json();

      // Verificar si hay más preguntas disponibles
      if (data.success && data.quiz && data.quiz.length > 0) {
        // Obtener datos del nuevo formato de JSON
        const quizData = data.quiz[0];

        // Asignar valores a las propiedades correspondientes
        this.correctAnswer = quizData.correct_answer;
        this.question = quizData.question;
        this.category = quizData.category;

        // Combina incorrect_answers y correct_answer, luego mezcla las opciones
        this.options = this.shuffleOptions([
          ...quizData.incorrect_answers.split(","),
          this.correctAnswer,
        ]);

        this.selectedOptionIndex = null; // Reset selected option
        this.resultMessage = ""; // Limpiar el mensaje de resultado
      } else {
        // No hay más preguntas, puedes mostrar un mensaje o realizar alguna acción
        console.log("No hay más preguntas disponibles.");
      }
    },
    shuffleOptions(options) {
      return options.sort(() => Math.random() - 0.5);
    },
    selectOption(index) {
      this.selectedOptionIndex = index;
    },
    checkAnswer() {
      if (this.selectedOptionIndex !== null) {
        const selectedAnswer = this.options[this.selectedOptionIndex];
        if (selectedAnswer === this.correctAnswer) {
          this.correctScore++;
          this.resultMessage = "<p><i class='fas fa-check'></i> ¡Correcto!</p>";
        } else {
          this.resultMessage = `
        <p><i class='fas fa-times'></i> ¡Incorrecto!</p>
        <small><b>Respuesta correcta: </b>${this.correctAnswer}</small>
      `;
        }
        this.checkCount();

        // Deshabilitar el botón durante el mismo tiempo que el setTimeout
        this.disableCheckButton = true;
        setTimeout(() => {
          this.disableCheckButton = false;
        }, 3000);
      } else {
        this.resultMessage =
          "<p><i class='fas fa-question'></i> Tienes que seleccionar una opción</p>";
      }
    },
    checkCount() {
      this.askedCount++;
      if (this.askedCount <= this.totalQuestion) {
        if (this.askedCount === this.totalQuestion) {
          this.resultMessage += `<p>Tu puntaje es ${this.correctScore}.</p>`;
        }
        setTimeout(() => {
          this.currentQuestionNumber++;
          this.loadQuestion();
        }, 2000);
      }
    },
    restartQuiz() {
      window.location.reload();
    },
  },
};
</script>
