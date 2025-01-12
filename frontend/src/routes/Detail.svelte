<script>
    import { get } from "svelte/store";
    import fastapi from "../lib/api"

    export let params = {}
    let question_id = params.question_id
    let question = {comments:[]}
    let content = ""

    function get_question() {
        fastapi('get', "/api/question/detail/" + question_id, {}, (json) => {
            question = json
        })
    }

    get_question()

    function post_comment() {
        event.preventDefault()
        let url = "/api/comment/create/" + question_id
        let params = {
            content: content
        }
        fastapi('post', url, params,
            (json) => {
                content = ''
                get_question()
            }
        )
    }
</script>

<div class="container my-3">
    <!-- 질문 -->
    <h2 class="border-bottom py-2">{question.subject}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{question.quest}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {question.create_date}
                </div>
            </div>
        </div>
    </div>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{question.answer}</div>
        </div>
    </div>
    <!-- 답변 목록 -->
    <h5 class="border-bottom my-3 py-2">{question.comments.length}개의 답변이 있습니다.</h5>
    {#each question.comments as comment}
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{comment.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {comment.create_date}
                </div>
            </div>
        </div>
    </div>
    {/each}
</div>