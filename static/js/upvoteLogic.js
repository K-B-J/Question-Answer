logic = (element) => {
    var inner_div = document.getElementById(String(element.id) + "-div")
    var inner_p = document.getElementById(String(element.id) + "-p")

    var url = String(window.location.href)
    var url_contents = url.split("/")
    var endPoint = url_contents[0] + "//" + url_contents[2]

    const request = new XMLHttpRequest()

    if (Array.from(inner_div.classList).includes("upvote", 0)) {
        endPoint = endPoint + "/upvote/" + String(element.id)
        request.open("GET", endPoint)
        request.send()
        request.onreadystatechange = () => {
            if (request.readyState == XMLHttpRequest.DONE) {
                inner_div.classList.remove("upvote")
                inner_div.classList.add("unupvote")
                inner_p.innerHTML = String(parseInt(inner_p.innerHTML) + 1)
            }
        }
    } else {
        endPoint = endPoint + "/unupvote/" + String(element.id)
        request.open("GET", endPoint)
        request.send()
        request.onreadystatechange = () => {
            if (request.readyState == XMLHttpRequest.DONE) {
                inner_div.classList.remove("unupvote")
                inner_div.classList.add("upvote")
                inner_p.innerHTML = String(parseInt(inner_p.innerHTML) - 1)
            }
        }
    }
}
