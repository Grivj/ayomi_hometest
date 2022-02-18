const updateForm = document.getElementById('update-email-form')
const inputEmail = document.getElementById('id_email')
const profileEmail = document.getElementById('profile_email')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const alertMessage = (type, message) => `
    <div class="alert alert-${type} alert-dismissible" role="alert">
        <strong>${message}</strong>
        <button
        type="button"
        class="close"
        data-dismiss="alert"
        aria-label="Close"
        >
        <span aria-hidden="true">&times;</span>
        </button>
    </div>
`

const handleAlerts = (type, message) => {
    const alertsBox = document.getElementById("alertsBox")
    alertsBox.innerHTML = alertMessage(type, message)
}


updateForm.addEventListener('submit', e => {
    e.preventDefault()
    console.log(inputEmail.value)
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('email', inputEmail.value)

    $.ajax({
        type: 'POST',
        url: "",
        data: fd,
        success: function (response) {
            handleAlerts(response.type, response.alert)
            $(profileEmail).html(response.updated_email)

        },
        error: function (response) {
            handleAlerts(response.type, response.errors[0])
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})