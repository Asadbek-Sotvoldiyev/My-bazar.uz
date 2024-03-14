$(function () {

    $("#contactForm input, #contactForm textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function ($form, event, errors) {
        },
        submitSuccess: function ($form, event) {
            event.preventDefault();
            var name = $("input#name").val();
            var email = $("input#email").val();
            var message = $("textarea#message").val();
            var url = $("#contactForm").data('url');
            var token = $("#contactForm").data('token');
            var user_email = $("#contactForm").data('user-email');

            if (email != user_email) {
                $('#success').html("<div class='alert alert-danger'>");
                $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                $('#success > .alert-danger').append($("<strong>").text("Kechirasiz, e-mail manzilingiz noto'g'ri. Iltimos tekshiring va qayta kiriting!"));
                $('#success > .alert-danger').append('</div>');
                return; // Stop further processing
            }

            $this = $("#sendMessageButton");
            $this.prop("disabled", true);

            $.ajax({
                url: url,
                type: "POST",
                data: {
                    name: name,
                    email: email,
                    message: message,
                    csrfmiddlewaretoken: token,
                    action:'post',
                },
                cache: false,
                success: function () {
                    $('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                            .append("</button>");
                    $('#success > .alert-success')
                            .append("<strong>Sizning xabaringiz muvaffaqiyatli yuborildi! </strong>");
                    $('#success > .alert-success')
                            .append('</div>');
                    $('#contactForm').trigger("reset");
                },
                error: function () {
                    $('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                            .append("</button>");
                    $('#success > .alert-danger').append($("<strong>").text("Kechirasiz " + name + ", bizning pochta serverimiz javob bermayotganga o'xshaydi. Iltimos keyinroq qayta urinib ko'ring!"));
                    $('#success > .alert-danger').append('</div>');
                    $('#contactForm').trigger("reset");
                },
                complete: function () {
                    setTimeout(function () {
                        $this.prop("disabled", false);
                    }, 1000);
                }
            });
        },
        filter: function () {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function (e) {
        e.preventDefault();
        $(this).tab("show");
    });
});

$('#name').focus(function () {
    $('#success').html('');
});
