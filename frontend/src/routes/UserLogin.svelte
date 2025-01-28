<script>
    import { push, link } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Title from "../assets/mock_turtle_soup.png"
    import Error from "../components/Error.svelte"
    import { access_token, username, is_login } from "../lib/store" 

    let error = {detail:[]}
    let login_username = ""
    let login_password = ""

    function login(event) {
        event.preventDefault()
        let url = "/api/user/login"
        let params = {
            username: login_username,
            password: login_password,
        }
        fastapi('login', url, params, 
            (json) => {
                $access_token = json.access_token
                $username = json.username
                $is_login = true
                push("/")
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>

<div class="form-signin">
  <form method="post">
    <div class="text-center">
      <img class="mb-4" src={Title} alt="Title" width="200px" height="40px"/>
      <h6 class="mb-4 border-bottom pb-3 fw-normal"><strong>바다거북스프 게임의 참가를 환영합니다.</strong></h6>
    </div>

    <div class="form-floating">
      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" bind:value="{login_username}">
      <label for="floatingInput">아이디</label>
    </div>

    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password" bind:value="{login_password}">
      <label for="floatingPassword">비밀번호</label>
    </div>

    <div class="justify-content-center">
      <button class="mt-2 mb-3 w-100 btn btn-lg btn-outline-primary" type="submit" on:click="{login}">Login</button>
      <button class="mb-3 w-100 btn btn-lg btn-outline-secondary"><a use:link class="nav-link" href="/user-create">회원가입</a></button>
    </div>
  </form>
</div>
