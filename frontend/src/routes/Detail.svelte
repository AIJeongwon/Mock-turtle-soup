<script>
    import { get } from "svelte/store";
    import fastapi from "../lib/api"
    import { is_login } from "../lib/store"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

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
                <div class="badge bg-light text-dark p-2 text-start">
                    <div class="mb-2">{ question.user ? question.user.username : ""}</div>
                    <div>{moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}</div>
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
                <div class="badge bg-light text-dark p-2 text-start">
                    <div class="mb-2">{ comment.user ? comment.user.username : ""}</div>
                    <div>{moment(comment.create_date).format("YYYY년 MM월 DD일 hh:mm a")}</div>
                </div>
            </div>
        </div>
    </div>
    {/each}
    <!-- 답변 등록 -->
    <form method="post" class="my-3">
        <div class="mb-3">
            <textarea rows="10" bind:value={content} 
                disabled={$is_login ? "" : "disabled"}
                class="form-control" />
        </div>
        <input type="submit" value="답변등록" class="btn btn-primary {$is_login ? '' : 'disabled'}" 
            on:click="{post_comment}" />
    </form>
</div>