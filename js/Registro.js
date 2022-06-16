$(document).ready(function() {
    $("#form-email").validate({
        rules:{
            email: {
                email: {
                    required: true,
                    email: true
                },
        menssage: {
            email: {
                email: "¡¡ERROR!! Debe tener sintaxis de email!!!"
            }
        }
            }
        }
    });
});