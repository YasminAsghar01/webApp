<template>
  <br /><br />
  <div class="well well-large">
    <h1>{{ item.title }}</h1>
    <img
      class="card-img-top"
      :src="'http://localhost:8000' + item.image"
      v-bind:alt="item.image"
      style="max-width: 50%"
    />
    <p>Description: {{ item.description }}</p>
    <p>Starting Price: {{ item.startingPrice }}</p>
    <p>Finish Date: {{ item.finishDate }}</p>
  </div>
  <br /><br />
  <form @submit.prevent="createPost" method="post">
    Ask a question:
    <br />
    <input
      type="text"
      name="question"
      placeholder="question.."
      v-model="question.question"
    />
    <button class="btn btn-sm bg-primary text-white btn-space" type="submit">
      Save
    </button>
  </form>
  <br /><br />
  <section>
    <h3 class="text-center mb-4 pb-2 text-primary fw-bold">
      Questions and answers
    </h3>
    <p class="text-center mb-5">
      Find questions other people have asked about this item below:
    </p>
    <div class="row gx-4 gx-lg-5">
      <div v-for="question in questions.answers" :key="question.id" class="col-md-4 mb-5">
        <span v-if="question.item == id">
          <div>
            <h6 class="mb-3 text-primary">
              <i class="far fa-paper-plane text-primary pe-2"></i>
              {{ question.question }}
            </h6>
            <span v-if="question.answer == null">
            </span>
            <div>
            <div>
                <div class="border rounded bg-info shadow p-4">
                  <form @submit.prevent="createAnswerPost(question)" method="post">
                    Answer:
                    <br />
                    <input
                      type="text"
                      name="answer"
                      placeholder="answer"
                      v-model="answer.answer"
                      /><br />
                  </form>
                </div>
            </div>
          </div>
            <span v-if="question.answer != null">
              <p>{{ question.answer }}</p>
            </span>
          </div>
        </span>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
export default {
  props: ["id", "user"],
  data() {
    return {
      item: [],
      questions: [],
      question: {
        question: null,
        id: this.id,
        user: this.user,
      },
      answer: {
        answer: null,
        id: this.id,
        user: this.user,
      }
    };
  },
  methods: {
    async getData() {
      let response = await fetch("http://localhost:8000/questions/");
      let data = await response.json();
      this.questions = data
    },
    async createPost() {
      let response = await fetch("http://localhost:8000/questions/", {
        method: "POST",
        content_type: "application/json",
        body: JSON.stringify(this.question),
      });
      if (response.ok) {
        this.getData()
        this.question.question = null
      } else alert("Could not add this question");

    },
    async createAnswerPost(question) {
      if (this.user == this.item.owner) {
        let response = await fetch("http://localhost:8000/questions/", {
          method: "POST",
          content_type: "application/json",
          body: JSON.stringify({ 'answer': this.answer, 'question': question }),
        });
        if (response.ok) {
          this.getData()
          this.answer.answer = null
        } else alert("Could not add this question");
      }
      else {
        alert("You are not the owner so cannot answer this question")
      }

    }
  },
  async mounted() {
    let response = await fetch("http://localhost:8000/item/" + this.id + "/");
    let response2 = await fetch("http://localhost:8000/questions/");
    let data = await response.json();
    let data2 = await response2.json();
    this.item = data;
    this.questions = data2;
  },
};
</script>
