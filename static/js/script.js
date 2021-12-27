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
    let cardCounter = 1;
    let cardId = 1;
    $("#add-card-button").click(function () {
        if (cardCounter < 30){

        $("#card-container").append(`
            '<div class="card grey lighten-5"><a class="remove-card-button right" href="#" onClick="return false;"><i class=" far fa-3x fa-times-circle red-text"></i></a><div class="card-content white-text"><div class="row"><div id="${cardId}-card-locator" class="col s12 m2 black-text"></div><div class="col s12 m4"><label for="${cardId}_card_front">English</label><input type="text" id="${cardId}_card_front" name="${cardId}_card_front" class="validate" required minlength="2" maxlength="32"></div><div class="col s12 m4"><label for="${cardId}_card_back">Translation</label><input type="text" id="${cardId}_card_back" name="${cardId}_card_back" class="validate" required minlength="2" maxlength="32"></div></div></div></div>'`);
        $("#add-card-button").attr("href", `#${cardCounter}-card-locator`)
       
        cardId++
        cardCounter++ 
        console.log("Card ID = " + cardId)
        console.log("Card Counter = " + cardCounter)
    }});

    // Clicking the remove-card-button removes a card from the form, and reduces the card counter.
    
    $(document).on("click", ".remove-card-button", function(){
    cardCounter--
    $(this).parent().remove()
    cardId--
    });

    // Card flip controller
    
    $(".flip-button").on("click", function(){
        $(this).parent().toggleClass("flipping");
        $(this).remove();
    })

    cardCounterEdit = $('#counter-class-container .counter-class').length
    cardIdEdit = $('#counter-class-container .counter-class').length
    console.log("Counter class: " +cardCounterEdit)

    $("#add-card-button-edit").click(function () {
        if (cardCounterEdit < 30){
            
        $(".card-container-edit").last().append(`
            '<div class="card grey lighten-5"><a class="remove-card-button right" href="#" onClick="return false;"><i class=" far fa-3x fa-times-circle red-text"></i></a><div class="card-content white-text"><div class="row"><div id="${cardIdEdit}-card-locator" class="col s12 m2 black-text"></div><div class="col s12 m4"><label for="${cardIdEdit}_card_front">English</label><input type="text" id="${cardIdEdit}_card_front" name="${cardIdEdit}_card_front" class="validate" required minlength="2" maxlength="32"></div><div class="col s12 m4"><label for="${cardIdEdit}_card_back">Translation</label><input type="text" id="${cardIdEdit}_card_back" name="${cardIdEdit}_card_back" class="validate" required minlength="2" maxlength="32"></div></div></div></div>'`);
        $("#add-card-button-edit").attr("href", `#${cardCounterEdit}-card-locator`)
       
        cardIdEdit++
        cardCounterEdit++ 
        console.log("Card ID Edit = " + cardIdEdit)
        console.log("Card Counter Edit = " + cardCounterEdit)
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