$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: 'right',
    });
    $('select').formSelect();
    $('.modal').modal();
    $(".dropdown-trigger").dropdown({
        coverTrigger: false
    });
    $('.collapsible').collapsible({
        accordion: true
    });
    $('#textarea1').val('New Text');
    $('.scrollspy').scrollSpy();
    let cardCounter = 2
    $("#add-card-button").click(function () {
        if (cardCounter <= 50){

        $("#card-container").append(`
            '<div class="card grey lighten-5"><div class="card-content white-text"><div class="row"><div class="col s12 m2 black-text"><h5 id="${cardCounter}-card-locator" class="center-align">Card ${cardCounter}</h5></div><div class="col s12 m4"><label for="${cardCounter}_card_front">English</label><input type="text" id="${cardCounter}_card_front" name="${cardCounter}_card_front"></div><div class="col s12 m4"><label for="${cardCounter}_card_back">Translation</label><input type="text" id="${cardCounter}_card_back" name="${cardCounter}_card_back"></div></div></div></div>'`);
        $("#add-card-button").attr("href", `#${cardCounter-1}-card-locator`)
        console.log(cardCounter)
        cardCounter++
    }});

});

// // The following code snippet has been taken from the Code Institute's video on Materialize Select Validation.
//  This code applies validation to select elements in the same style as other Materialize from elements.
$(document).ready(function () {
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});