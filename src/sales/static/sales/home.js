const reportForm = document.getElementById('report-form')
const reportBtn = document.getElementById("report-btn")
const img = document.getElementById('img')
const btn = document.getElementById('sub')
const modalBody = document.getElementById('modal-body')
const reportName= document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const alertBox = document.getElementById('alert-box')

const handleAlerts = (type, msg)=>{
    alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                            ${msg}
                        </div>`
}
console.log(csrf)
if(img){
    reportBtn.classList.remove('not-visible')

}

reportBtn.addEventListener('click', ()=>
{
    img.setAttribute('class', 'w-100')
    modalBody.prepend(img)

    reportForm.addEventListener('submit', e=>{
        e.preventDefault()
        const formData = new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('name', reportName.value)
        formData.append('remarks', reportRemarks.value)
        formData.append('image', img.src)

        $.ajax({
            type:'POST', 
            url:'/reports/save/',
            data: formData,
            success: function(response){
                console.log(response)
                handleAlerts('success','Report has been created')
                reportForm.reset();
            },
            error: function(error){
                console.log(error)
                handleAlerts('danger','Opps ......somethin went wrong')
            },
            processData:false,
            contentType:false
        })
    })
})







