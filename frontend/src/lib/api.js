const fastapi = (operation, url, params, sucess_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    let _url = import.meta.env.VITE_SERVER_URL + url
    if (method === 'get') {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-type": content_type
        }
    }

    if (method !== 'get') {
        options['body'] = body
    }

    fetch(_url, options)
        .then(response => {
            if (response.status === 204) { // NO CONTENT
                if (sucess_callback) {
                    sucess_callback()
                }
                return
            }
            response.json()
                .then(json => {
                    if (response.status >= 200 && response.status < 300) {
                        if (sucess_callback) {
                            sucess_callback(json)
                        }
                    }
                    else {
                        if (failure_callback) {
                            failure_callback(json)
                        }
                        else {
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi