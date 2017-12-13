// Wait for the DOM to be ready
$(function() {

    /*
    *****
    Refer this to add Form Validations in this script
    Validation rules list can be find here: https://jqueryvalidation.org/documentation/
    *****

    $("form[name='name_of_the_form']").validate({
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            key_name: {
                required: true,
            }
        },
        // Specify validation error messages
        messages: {
            key_name: {
                required: "Please provide a username",
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function(form) {
            form.submit();
        }
    });
    */

    // Initialize form validation on the login form.
    $("form[name='login']").validate({
        rules: {
            username: {
                required: true,
                minlength: 4,
                maxlength: 30,
                alphanumeric: true
            },
            password: {
                required: true,
                minlength: 7
            }
        },
        messages: {
            username: {
                required: "Please enter your username",
                minlength: "Minimum 4 characters",
                maxlength: "Maximum 30 characters",
                alphanumeric: "Please enter a valid username"
            },
            password: {
                required: "Please enter your password",
                minlength: "Must be more than 6 characters"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });
});

try{
    $.validator.addMethod( 'alphanumeric', function(value, element) {
        var username = $("#id_username").val();
        var regex = /^(?![0-9]*$)[a-zA-Z0-9-.&_]+$/;
        return regex.test(username);

    });
}
catch(e){
    console.log(e);
}

var remove_error_message = function(){
    $("#not_match").html("");
}
