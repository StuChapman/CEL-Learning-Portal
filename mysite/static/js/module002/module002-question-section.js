// jshint esversion: 6

// ********************************** Question Section Functions ********************************** //

// ********** General Functions ********** //

// ********************************** Unused - to be deleted ********************************** //

//Function: check the answers against desired for radio button style questions: one, three and eight //
function checkQuestionRadio() {
    const rbs = document.querySelectorAll('input[name="question"]'); //Credit: https://www.javascripttutorial.net/javascript-dom/javascript-radio-button/ //
    let selectedValue;
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.id;
            break;
        }
    }
    revealNext();
    $('input[name="testanswer"]').val(selectedValue);
    let thisquestion = document.title;

    // answers to radio button style questions: one, three and eight //
    switch(thisquestion) {
        case 'Online Learning - Question 1':
            if (selectedValue == 'optionfour') {
                answerFlag1 = 1;
            } else {
                answerFlag1 = -1;
            }
            localStorage.setItem('answerFlag1', answerFlag1);
            break;
        case 'Online Learning - Question 3':
            if (selectedValue == 'optiontwo') {
                answerFlag3 = 1;
            } else {
                answerFlag3 = -1;
            }
            localStorage.setItem('answerFlag3', answerFlag3);
            break;
        case 'Online Learning - Question 8':
            if (selectedValue == 'optionthree') {
                answerFlag8 = 1;
            } else {
                answerFlag8 = -1;
            }
            localStorage.setItem('answerFlag8', answerFlag8);
            break;
        default:
            break;
    }
}

//Function: check the answer against desired for questions: two and six //
function populateMuda(letterpick) {

    // if selected letter has already been chosen and is gray-ed out, exit function //
    let letterString = "#letterpick-" + letterpick;

    if($(letterString).css('color') == 'rgb(128, 128, 128)'){
        return;
    }

    $(letterString).css('color', 'gray');
    if(letterpick.length < 3){
        letterpick = letterpick.substring(0, 1);
    }

    if($.trim($('#square-one').text())==''){ // Credit: https://stackoverflow.com/questions/6813227/how-do-i-check-if-an-html-element-is-empty-using-jquery //
        $('#square-one').text(letterpick);
        $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
    } else {
        if($.trim($('#square-two').text())==''){
            $('#square-two').text(letterpick);
            $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
        } else {
            if($.trim($('#square-three').text())==''){
                $('#square-three').text(letterpick);
                $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
            } else {
                if($.trim($('#square-four').text())==''){
                    $('#square-four').text(letterpick);
                    $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                } else {
                    if($.trim($('#square-five').text())==''){
                        $('#square-five').text(letterpick);
                        $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                    } else {
                        if($.trim($('#square-six').text())==''){
                            $('#square-six').text(letterpick);
                            $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                        } else {
                            if($.trim($('#square-seven').text())==''){
                                $('#square-seven').text(letterpick);
                                $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                            } else {
                                if($.trim($('#square-eight').text())==''){
                                    $('#square-eight').text(letterpick);
                                    $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                                } else {
                                    if($.trim($('#square-nine').text())==''){
                                        $('#square-nine').text(letterpick);
                                        $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                                    } else {
                                        if($.trim($('#square-ten').text())==''){
                                            $('#square-ten').text(letterpick);
                                            $('input[name="testanswer"]').val($('input[name="testanswer"]').val()+letterpick);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    letterCount = ++letterCount;

    if(letterpick.length < 3){
        if (letterCount == 10) {
            letterCount = 0;
            revealNext();
            return;
        }
    } else {
        if (letterCount == 4) {
            letterCount = 0;
            revealNext();
            return;
        }
    }
}

//Function: allow the user to reset if they want to change their answer on question: two and six //
function resetMuda() {
    $('#square-one').text('');
    $('#square-two').text('');
    $('#square-three').text('');
    $('#square-four').text('');
    $('#square-five').text('');
    $('#square-six').text('');
    $('#square-seven').text('');
    $('#square-eight').text('');
    $('#square-nine').text('');
    $('#square-ten').text('');
    $('.letterpickbox div').css('color', 'black');
    $('.wordpickbox div').css('color', 'black');
    $('input[name="testanswer"]').val('');
    $("#testanswerbtn").addClass("hidden");
    $("#testanswerbtn").removeClass("unhidden");
}

//Function: check answers against desired on checkbox questions: four, seven and ten //
function checkQuestionCheckbox() {

    revealNext();
    $('input[name="testanswer"]').val('');
    let selectedValue = '';
    let thisquestion = document.title;

    if ($('#checkone').is(":checked")) {
        selectedValue = selectedValue + "checkone"
        $('input[name="testanswer"]').val(selectedValue);
    }
    if ($('#checktwo').is(":checked")) {
        selectedValue = selectedValue + "checktwo"
        $('input[name="testanswer"]').val(selectedValue);
    }
    if ($('#checkthree').is(":checked")) {
        selectedValue = selectedValue + "checkthree"
        $('input[name="testanswer"]').val(selectedValue);
    }
    if ($('#checkfour').is(":checked")) {
        selectedValue = selectedValue + "checkfour"
        $('input[name="testanswer"]').val(selectedValue);
    }

    switch(thisquestion) {
        case 'Online Learning - Question 4':
            if (!$('#checkone').is(":checked") && $('#checktwo').is(":checked") && !$('#checkthree').is(":checked") && $('#checkfour').is(":checked")) {
                $('input[name="testanswer"]').val(selectedValue);
                answerFlag4 = 1;
            } else {
                answerFlag4 = -1;
            }
            localStorage.setItem('answerFlag4', answerFlag4);
            break;
        case 'Online Learning - Question 7':
            if (!$('#checkone').is(":checked") && !$('#checktwo').is(":checked") && $('#checkthree').is(":checked") && $('#checkfour').is(":checked")) {
                answerFlag7 = 1;
            } else {
                answerFlag7 = -1;
            }
            localStorage.setItem('answerFlag7', answerFlag7);
            break;
        case 'Online Learning - Question 10':
            if ($('#checkone').is(":checked") && !$('#checktwo').is(":checked") && !$('#checkthree').is(":checked") && $('#checkfour').is(":checked")) {
                answerFlag10 = 1;
            } else {
                answerFlag10 = -1;
            }
            localStorage.setItem('answerFlag10', answerFlag10);
            break;
    }
}

//Function: allow drag event on question-five.html //
function drag(ev) {// credit to https://www.w3schools.com/HTML/html5_draganddrop.asp
    ev.dataTransfer.setData("text", ev.target.id);
}

//Function: allow drop event on question-five.html //
function allowDrop(ev) {// credit to https://www.w3schools.com/HTML/html5_draganddrop.asp
    ev.preventDefault();
}

//Function: determine drop locations on question-five.html //
function drop(ev) {// credit to https://www.w3schools.com/HTML/html5_draganddrop.asp
    ev.preventDefault();

    $('#' + dragcard1).attr('ondragover', "");
    let data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));

    let dragVar;
    dragVar = ev.target.id;
    // do not allow more than one card to be dropped into each box //
    $('#' + dragVar).attr('ondragover', "");
    
    switch (data) {
    case 'dragcard1': 
        dragcard1 = ev.target.id.slice(0, -1) + "1";
        break;
    case 'dragcard2': 
        dragcard2 = ev.target.id.slice(0, -1) + "2";
        break;
    case 'dragcard3': 
        dragcard3 = ev.target.id.slice(0, -1) + "3";
        break;
    case 'dragcard4': 
        dragcard4 = ev.target.id.slice(0, -1) + "4";
        break;
    case 'dragcard5': 
        dragcard5 = ev.target.id.slice(0, -1) + "5";
        break;
    default: 
        break;
    }

    if (dragcard1 !== null && dragcard2 !== null && dragcard3 !== null && dragcard4 !== null && dragcard5 !== null) {
        $('input[name="testanswer"]').val(dragcard1+dragcard2+dragcard3+dragcard4+dragcard5);
        revealNext();
    }
}

//Function: check drop locations against desired on question-five.html //
function checkQuestionDragDrop() {
    if (dragcard1.substring(4, 8) == 'left') {
        drag1Score = 1;
    } else {
        drag1Score = -1;
    }
    if (dragcard2.substring(4, 8) == 'righ') {
        drag2Score = 1;
    } else {
        drag2Score = -1;
    }
    if (dragcard3.substring(4, 8) == 'righ') {
        drag3Score = 1;
    } else {
        drag3Score = -1;
    }
    if (dragcard4.substring(4, 8) == 'left') {
        drag4Score = 1;
    } else {
        drag4Score = -1;
    }
    if (dragcard5.substring(4, 8) == 'righ') {
        drag5Score = 1;
    } else {
        drag5Score = -1;
    }

    if (drag1Score + drag2Score + drag3Score + drag4Score + drag5Score == 5) {
        answerFlag5 = 1;
    } else {
        answerFlag5 = -1;
    }

    // write answer to local storage //
    localStorage.setItem('answerFlag5', answerFlag5);

}

//Function: allow drag event on question-nine.html //
function dragOrder(ev) {// credit to https://www.w3schools.com/HTML/html5_draganddrop.asp //
    ev.dataTransfer.setData("text", ev.target.id);

    let i = getIndexOfK(orderArray, ev.target.id);
    orderArray[i][3] = 'vacated';

}

//Function: determine drop locations on question-nine.html //
function order(ev) {
    ev.preventDefault();

    let i = getIndexOfK(orderArray, ev.target.id);
    let j = getIndexOfK(orderArray, 'vacated');

    // get the box, card and text that we are dragging //
    let orderboxDrag = orderArray[j][0];
    let ordercardDrag = orderArray[j][1];
    let ordertextDrag = orderArray[j][2];

    // get the box, card and text that we are need to shift from the dragged to the vacated box //
    let orderboxShift = orderArray[i][0];
    let ordercardShift = orderArray[i][1];
    let ordertextShift = orderArray[i][2];
    
    // repopulate orderArray //
    orderArray[i][1] = ordercardDrag;
    orderArray[i][2] = ordertextDrag;
    orderArray[j][3] = 'full';
    orderArray[j][1] = ordercardShift;
    orderArray[j][2] = ordertextShift;
    
    // populate the box, card and text that have been dragged and shifted //
    document.getElementById(orderboxShift).innerHTML = '<div class="ordercard align-vertically" id="' + ordercardDrag + '" draggable="true" ondragstart="dragOrder(event)" >' + ordertextDrag + '</div>';
    document.getElementById(orderboxDrag).innerHTML = '<div class="ordercard align-vertically" id="' + ordercardShift + '" draggable="true" ondragstart="dragOrder(event)" >' + ordertextShift + '</div>';

    $('input[name="testanswer"]').val(orderArray[0][1]+orderArray[0][1]+orderArray[2][1]+orderArray[3][1]+orderArray[4][1]+orderArray[5][1]+orderArray[6][1]+orderArray[7][1]);
    revealNext();

}

//Function: check order against desired on question-nine.html //
function checkQuestionOrder() {
if ( orderArray[0][1] == 'ordercard4'  && orderArray[1][1] == 'ordercard8' && orderArray[2][1] == 'ordercard6' && orderArray[3][1] == 'ordercard7' && orderArray[4][1] == 'ordercard1' && orderArray[5][1] == 'ordercard5' && orderArray[6][1] == 'ordercard3' && orderArray[7][1] == 'ordercard2') {
    answerFlag9 = 1;
    } else {
    answerFlag9 = -1; 
    }

    localStorage.setItem('answerFlag9', answerFlag9);

}

//Function: confirm two checkboxes have been checked before revealing submit on question-ten.html //
function checkTwo() {
    let checkCount = 0;
    if ($('#checkone').is(":checked")) {
        ++checkCount;
    }
    if ($('#checktwo').is(":checked")) {
        ++checkCount;
    }
    if ($('#checkthree').is(":checked")) {
        ++checkCount;
    }
    if ($('#checkfour').is(":checked")) {
        ++checkCount;
    }

    if (checkCount > 1) {
        checkQuestionCheckbox();
    }
}

//Function: populate test results on test-summary.html //
function populateSummary() {
    let totalScore = 0;
    let result;
    let resultColor;
    let answerVar;
    let answerSpan;
    let i;

    for (i = 0; i < 11; i++) {
        answerVar = 'answerFlag' + i;
        switch (localStorage.getItem(answerVar)) {
            case '-1':
                result = '<i class="fas fa-times"></i>';
                resultColor = 'red';
                break;
            case '0':
                result = '<i class="fas fa-minus"></i>';
                resultColor = 'gray';
                break;
            case '1':
                result = '<i class="fas fa-check"></i>';
                resultColor = 'green';
                ++totalScore;
                break;
            default: 
                break;
        }
        answerSpan = '#answer' + i;
        $(answerSpan).css('color', resultColor);
        $(answerSpan).html(result);
    }

    localStorage.setItem('totalScore', totalScore);
    $('#totalScore').text(totalScore + ' out of 10');

    if (totalScore < 7) {
        $('#retestbutton').text('Retake Test');
    }
}

//Function: either return to start of test or print certificate on test-summary.html //
function resetPrint() {

    let resetPrint = $('#retestbutton').text();

    switch (resetPrint) {
            case 'Retake Test':
                resetAnswerFlags();
                window.location.replace('test-intro.html');
                break;
            case 'Print Certificate':
                window.location.replace('test-certificate.html');
                break;
            default: 
                break;
        }
}