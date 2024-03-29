// jshint esversion: 6

// ********************************** Interactive Learning Section Functions ********************************** //

// ********** General Functions ********** //

// Function: find index of multidimensional array //
function getIndexOfK(arr, k) { //credit to https://jsfiddle.net/wao20/Lct1de56/ via https://stackoverflow.com/questions/16102263/to-find-index-of-multidimensional-array-in-javascript
    for (var i = 0; i < arr.length; i++) {
        var index = arr[i].indexOf(k);
        if (index > -1) {
        return i;
        }
    }
}

// ********** View specific Functions ********** //

//Function: using the play button to play and pause the condensation video on page002module002 //
function playVid() { 

    let buttonText = $("#playbutton").text();
    let playText = $.trim(buttonText);

    switch(playText) {
        case "play":
            player.playVideo();
            $("#playbutton").text("pause");
            break;
        case "pause":
            player.pauseVideo();
            $("#playbutton").text("play");
            break;
        default:
            break;
    }
}

//Function: reset button from pause to play when the video finishes on page002module002 //
function resetPlay() {
    $("#playbutton").text("play");
}

//Function: reveal the definition for Value by clicking the word value on page003module002 //
function revealValue() {

    nextRevealValue++;
    nextReveal = nextRevealValue * nextRevealWaste;

    if (nextReveal > 0) {
        $("#arrowsub").text("Obviously, treatment and cleaning are no substitute for prevention, but keeping on top of mould before it spreads can improve quality of life in the home. You are now ready to complete the online test...");
        revealNext();
    }
    $("#arrowmaskwaste").animate({ //Credit: https://www.tutorialrepublic.com/codelab.php?topic=faq&file=jquery-slide-left-and-right-effect
                width: '33vw'
            });
    $("#arrowmaskvalue").animate({ //Credit: https://www.tutorialrepublic.com/codelab.php?topic=faq&file=jquery-slide-left-and-right-effect
                width: 0
            });
}

//Function: reveal the definition for Waste by clicking the word waste on page003module002 //
function revealWaste() {

    nextRevealWaste++;
    // confirm that both definitions have been viewed before revealing next href //
    nextReveal = nextRevealValue * nextRevealWaste;

    if (nextReveal > 0) {
        $("#arrowsub").text("Obviously, treatment and cleaning are no substitute for prevention, but keeping on top of mould before it spreads can improve quality of life in the home. You are now ready to complete the online test...");
        revealNext();
    }
    $("#arrowmaskvalue").animate({ //Credit: https://www.tutorialrepublic.com/codelab.php?topic=faq&file=jquery-slide-left-and-right-effect
                width: '33vw'
            });
    $("#arrowmaskwaste").animate({ //Credit: https://www.tutorialrepublic.com/codelab.php?topic=faq&file=jquery-slide-left-and-right-effect
                width: 0
            });
}

//Function: scroll to next image on page004module002 //
function nextImage(getpage) {
    if (imageCount == 4) {
          imageCount = 4;
        } else {
          imageCount++;
        }
    populateImage(getpage);
}

//Function: scroll to previous image on page004module002 //
function prevImage(getpage) {
    if (imageCount == 0) {
          imageCount = 0;
        } else {
          imageCount--;
        }
    populateImage(getpage);
}

//Function: set the image and text on page004module002 and page005module002 //
function populateImage(getpage) {
    switch(getpage) {
        case 1:
            imageArray = 
                [
                    ['kettle', 'Water vapour can come from many sources, for example: a kettle', '<a class="attribute" target="_blank" href="https://www.freepik.com/free-vector/sticker-template-kettle-with-boiling-water-isolated_18376252.htm">Image by brgfx</a> on Freepik'],
                    ['steam', 'The steam from the kettle will disappear into the air','<a class="attribute" target="_blank" href="https://www.freepik.com/free-photo/drop-gray-paint-falling-water_995087.htm">Image by onlyyouqj</a> on Freepik'],
                    ['humidity', 'The air in the home now becomes more humid as a result of the steam','image copyright'],
                    ['condensation', 'The humid air will condense into water droplets when it comes in contact with a cold surface','<a class="attribute"  target="_blank" href="https://www.freepik.com/free-photo/water-drops-texture-background-white-design_18998782.htm">Image by rawpixel.com</a> on Freepik'],
                    ['sources', 'There are many sources of condensation in the home. Not all of them are obvious...','<a class="attribute"  target="_blank" href="https://www.freepik.com/free-vector/illustration-list_2945066.htm">Image by rawpixel.com</a> on Freepik']
                ];
            break;
        case 2:
            imageArray = 
                [
                    ['window', 'Windows are one of the coldest surfaces in the home. One way to minimise this; is for radiators to be located below windows.'],
                    ['external', 'External walls tend to be colder than internal - you can see in the image, the mould is only on one wall (external) and the other (internal) is mould free. Again, locating radiators on external walls will help.'],
                    ['thermal', 'External walls can be even colder if there is a lack of cavity insulation, or the insulation has been breached by some building material (a beam, joist, block etc.) A cavity inspection or use of thermal imaging as shown, will indicate any remedial work that would be required.'],
                    ['ceiling', 'Upstairs ceilings are another colder surface, especially if the loft insulation is missing or inadequate. Mould is common around the edges of a ceiling, where the loft insulation has not been pushed all the way into the eaves, causing a cold gap. Relaying or replacing the loft insulation will help.'],
                    ['furniture', 'Behind furniture is not a cold spot specifically, more the humid air get trapped behind and eventually condenses onto the wall. It can be a problem because the mould is unseen and grows for a long time. Moving furniture away from the wall (even by a centimeter) helps. ']
                ];
            break;
        default:
            break;
    }

    $("#valueimage").attr('src', '/media//module002/' + imageArray[imageCount][0] + '.jpg'); //Credit: https://www.juniordevelopercentral.com/jquery-change-image-src/#:~:text=jQuery%20change%20image%20src%20-%20How%20To%20Change,as%20simple%20as%20using%20the%20attr%20%2Afunction.%20 //

    // 200ms delay to allow image to cache //
    setTimeout(function() {
        switch(getpage) {
            case 1:
                $("#imagetext").text(imageArray[imageCount][1]);
                $("#attribute").html(imageArray[imageCount][2]);
                break;
            case 2:
                $("#imagedetail").text(imageArray[imageCount][1]);
                break;
        }
    }, 200);

    let colorTagLeft;
    let colorTagRight;

    switch(imageCount) {
        case 0:
            colorTagLeft = '#eeeeee';
            break;
        case 1:
            colorTagLeft = '#657486';
            break;
        case 3:
            colorTagRight = '#657486';
            break;
        case 4:
            colorTagRight = '#eeeeee';
            revealNext();
            break;
        default:
            break;
    }

    $("#leftcarouselarrow").css('color', colorTagLeft);
    $("#rightcarouselarrow").css('color', colorTagRight);
}

//Function: reveal the additional text on page006module002 //
function scrollDown() {
    $('#scrollone').css('display', 'none');
    $('#scrolltwo').css('display', 'block');
    revealNext();
}

//Function: hide the additional text on page006module002 //
function scrollUp() {
    $('#scrollone').css('display', 'block');
    $('#scrolltwo').css('display', 'none');
}

//Function: handle the images on page007module002 ready for the popup //
function handleWaste(imagetag) {

    let imageString = imagetag.substr(1) + 'Flag'; //Credit: https://stackoverflow.com/questions/4564414/delete-first-character-of-a-string-in-javascript

    // as each image is clicked, populate its variable to 1 //
    switch(imageString) {
        case 'kettle2Flag':
            transportationFlag = 1;
            break;
        case 'anemometerFlag':
            transportationFlag = 1;
            break;
        case 'saucepanFlag':
            inventoryFlag = 1;
            break;
        case 'hygrometer2Flag':
            inventoryFlag = 1;
            break;
        case 'clothesFlag':
            motionFlag = 1;
            break;
        case 'thermal2Flag':
            motionFlag = 1;
            break;
        case 'showerFlag':
            waitingFlag = 1;
            break;
        case 'moistureFlag':
            waitingFlag = 1;
            break;
        case 'washingFlag':
            overproductionFlag = 1;
            break;
        case 'dampproofFlag':
            overproductionFlag = 1;
            break;
        case 'mortarFlag':
            overprocessingFlag = 1;
            break;
        case 'leakFlag':
            defectsFlag = 1;
            break;
        case 'vegetationFlag':
            defectsFlag = 1;
            break;
        case 'breathFlag':
            skillsFlag = 1;
            break;
        case 'ventilationFlag':
            skillsFlag = 1;
            break;
        default:
            break;
    }

    // confirm that all popups have been viewed before revealing next anchor //
    // as this is a product, clickCount is only 1 once all images are clicked //
    let clickCount = (transportationFlag * inventoryFlag * motionFlag * waitingFlag * overproductionFlag * overprocessingFlag * defectsFlag * skillsFlag);

    if (clickCount == 1) {
    revealNext();
    }

    // change opacity of clicked image to show status as clicked //
    $(imagetag).css('opacity', 0.25); //Credit: https://stackoverflow.com/questions/2396342/transparent-image-is-it-possible-in-js

    popupWaste(imagetag);
}

//Function: reveal and populate the detailed description of each waste on page004module002 and page009module002 //
function popupWaste(imagetag) {

    let indexString = imagetag.substr(1);
    let wasteIndex =0;

    let popupArray = [
                    ['Kettle Boiling', 'As previously mentioned, steam will make the surrounding air humid.', 
                        'Turning on the extractor fan, opening a window and keeping the kitchen door closed can all minimise the risk.', 
                            '...remember, the humidity may be caused in the kitchen, but the condensation could appear in a different room.'],
                    ['Cooking', 'Similarly to a kettle, steam from pans or the oven, will make the surrounding air humid.', 
                        'Again, turn on the extractor fan, open a window and keep the kitchen door closed to reduce the risk.', 
                            '...do all three if you can.'],
                    ['Drying Clothes', 'Most people dry their clothes inside the home from time to time.', 
                        'A single load of washing typically contains 2 litres of water which if dried internally, will become airborne .', 
                            '...drying clothes in a utility room or bathroom, with an extraction fan on, will help remove the moisture to outside the home.'],
                    ['Bathing', 'Running the bath, shower and hot taps produce steam.', 
                        'The bathroom extractor fan should always be on when hot water is running, and the bathroom door closed.', 
                            '...even better - open a window as well, to let all the steam escape.'],
                    ['Laundry', 'Washing Machines and Tumble Driers create steam.', 
                        'Both utilities should be vented appropriately.', 
                            '...windows, fans and doors can help prevent the steam from spreading to other rooms.'],
                    ['Damaged Brick Work', 'Water can get into the home from outside.', 
                        'Missing mortar or cracks, or an ineffective or damaged Damp Proof Course should be inspected and repaired.', 
                            '...a walk around your home could identify sources of moisture.'],
                    ['Pipe or Roof Leaks', 'Another source of moisture from outside the home.', 
                        'The fabric of the building will absorb water, which will then evaporate into the air.', 
                            '...a pipe leak under a bathroom sink could cause condensation in a different room.'],
                    ['Breathing!', 'As in the video we saw earlier.', 
                        'Humans breathe out about a litre of water a day. Dogs and cats too!', 
                            '...overcrowding can be a major source of condensation if too many people share one home.'],
                    ['Anemometer', 'Air flow, in litres per second, through a fan, using an Anemometer.', 
                        'More accurate than using a piece of tissue paper!', 
                            '...will reveal whether the fan is working to specification and if it is the correct fan for the room size.'],
                    ['Hygrometer', 'Air Temperature and Relative Humidity, with a Hygrometer.', 
                        'Can be bought relatively cheaply (£10 for 3). Sets a baseline for each room within the home.', 
                            '...can actually vary a lot depending on: the weather, time-of-day, whether the heating is on etc.'],
                    ['Thermal Imaging', 'To identify cold spots...', 
                        '...where cavity insulation has been breached or doesn`t exist, where loft insulation is missing.', 
                            '...can be used to predict where mould will form in colder months.'],
                    ['Moisture Content', 'Within a wall', 
                        '...Can indicate the presence of water, from a leak, or getting in from outside.', 
                            '...may not be in the same room as the mould!'],
                    ['Damp Proof Course', 'A membrane that prevents moisure from the ground getting into the home.', 
                        'A damaged, missing or ineffective Damp Proof Course can be a major source of water ingress.', 
                            '...can have a significant effect on the property.'],
                    ['Obstructions', 'Either blocking sunlight or damaging the brickwork.', 
                        'Anything that is against an external wall can be a problem. Rubbish bags or a bin can block the light and keep the wall cooler that it could be.', 
                            'Vegetation can grow into cracks in the bricks and mortar and cause problems.'],
                    ['General Ventilation', 'The survey will review the ventilation in all rooms.', 
                        '... are there trickle vents? Are they open? Is the fan switched off at the isolator? Is there a fan? Does it get used?', 
                            'General conditions, such as: the drying of clothes, overcrowding and thermostat settings will be considered too.'],
                ];
    
    switch(indexString) {
        case 'kettle2':
            wasteIndex = 0;
            break;
        case 'saucepan':
            wasteIndex = 1;
            break;
        case 'clothes':
            wasteIndex = 2;
            break;
        case 'shower':
            wasteIndex = 3;
            break;
        case 'washing':
            wasteIndex = 4;
            break;
        case 'mortar':
            wasteIndex = 5;
            break;
        case 'leak':
            wasteIndex = 6;
            break;
        case 'breath':
            wasteIndex = 7;
            break;
        case 'anemometer':
            wasteIndex = 8;
            break;
        case 'hygrometer2':
            wasteIndex = 9;
            break;
        case 'thermal2':
            wasteIndex = 10;
            break;
        case 'moisture':
            wasteIndex = 11;
            break;
        case 'dampproof':
            wasteIndex = 12;
            break;
        case 'vegetation':
            wasteIndex = 13;
            break;
        case 'ventilation':
            wasteIndex = 14;
            break;
        default:
            break;
    }

    $('#pophead').text(popupArray[wasteIndex][0]);
    $('#poppone').text(popupArray[wasteIndex][1]);
    $('#popptwo').text(popupArray[wasteIndex][2]);
    $('#wastepopupimage').attr('src', '/media/module002/' + indexString + '.jpg');
    $('#poppthree').text(popupArray[wasteIndex][3]);
    // 200ms delay to allow image to cache //
    setTimeout(function() {
        $('#wastepopup').css('visibility', 'visible');
    }, 200); 
}

//Function: hide the detailed description of each waste on page007module002 //
function popDownWaste() {
    $('#wastepopup').css('visibility', 'hidden');
}

//Function: work through the steps in page008module002 //
function exampleSelect() {
    exampleStepNo = $.trim($('#examplestep').text().substring(0, 1));

    let answerindex = examplearray[exampleStepNo - 1][1];
    let answertext = examplearray[exampleStepNo - 1][2];

    var exampleindex  = examplelist.selectedIndex; // Credit: https://www.codeproject.com/articles/656/using-javascript-to-handle-drop-down-list-selectio //

    if (exampleindex == answerindex) {
        $('#examplestep').html('Thats right! ' + answertext);
    } else {
        $('#examplestep').html('Not quite. ' + answertext);
    }

    if (exampleStepNo == 4) {
        $('#examplepara').text('Hygrometers are really useful in helping to manage humidity, and could be used in every room.');
        $('#examplelist').css('visibility', 'hidden');
        $("#examplecarouselarrow").css('color', '#dddcdc');
        revealNext();
    } else {
        $('#examplepara').text('tap the arrow to move to the next step...');
        $('#examplelist').css('visibility', 'hidden');
        $("#examplecarouselarrow").css('color', '#657486');
    }
}

//Function: navigate to the next step in page008module002 //
function nextExample() {
    if ($("#examplecarouselarrow").css('color') == 'rgb(221, 220, 220)') {
        return;
    } else {
        ++exampleStepNo;
        $('#examplestep').html(examplearray[exampleStepNo - 1][0]);
        document.getElementById("examplelist").selectedIndex = "0";
        $('#examplelist').css('visibility', 'visible');
        $("#examplecarouselarrow").css('color', '#dddcdc');
        $('#examplepara').text('What action should we take to bring the humidity down? Select from the list below...');
    }
}

// ********************************** Unused - to be deleted ********************************** //

// Function: reset answerflags - ADMIN ONLY //
function resetAnswerFlags() {
    var i;
    for (i = 0; i < 11; i++) {
        localStorage.setItem('answerFlag' + i, 0);
        }
}

//Function: get the user's name and email to pass to the test pass certificate (validate at a later date) //
function logIn() {
    if (!/^[a-zA-Z]*$/g.test(this.usernamefirst.value) || this.usernamefirst.value == "") {
        alert('Please enter your first name, with no spaces or numbers.');
        this.usernamefirst.focus();
        return;
    }
    if (!/^[a-zA-Z]*$/g.test(this.usernamelast.value) || this.usernamelast.value == "") {
        alert('Please enter your last name, with no spaces or numbers.');
        this.usernamelast.focus();
        return;
    }
    if (!(/^\S+@\S+\.\S+$/.test(this.useremail.value))) {
        alert('Please enter a valid email address.');
        this.useremail.focus();
        return;
    }
    localStorage.setItem('username', this.usernamefirst.value + " " + this.usernamelast.value);
    localStorage.setItem('useremail', this.useremail.value);

    alert('Welcome ' + this.usernamefirst.value + " " + this.usernamelast.value + '. Tap ok to start.');
    window.location.replace('intro.html');
}

// Function: check quiz score progress on document load //
$(window).on('pageshow', function() {

    // check this question has not already been answered //
    let thisquestion = document.title.substr(18,11);

    let questionarray = [['Question 1',  'answerFlag1', 'question-two.html'],
                        ['Question 2',  'answerFlag2', 'question-three.html'],
                        ['Question 3',  'answerFlag3', 'question-four.html'],
                        ['Question 4',  'answerFlag4', 'question-five.html'],
                        ['Question 5',  'answerFlag5', 'question-six.html'],
                        ['Question 6',  'answerFlag6', 'question-seven.html'],
                        ['Question 7',  'answerFlag7', 'question-eight.html'],
                        ['Question 8',  'answerFlag8', 'question-nine.html'],
                        ['Question 9',  'answerFlag9', 'question-ten.html'],
                        ['Question 10',  'answerFlag10', 'test-summary.html']];

    if (thisquestion == 'Test Summar') {
        populateSummary();
    }

    if (thisquestion == 'Certificate') {
        $('#certName').text(localStorage.getItem('username'));
        $('#totalScore').text(localStorage.getItem('totalScore') + ' out of 10.');
        alert('Here is your certificate. After printing, you can simply close your browser.');
    }

    let i = getIndexOfK(questionarray, thisquestion);
    // exit function if i is undefined //
    if(i == null){
        return;
    } 

    let j = questionarray[i][1];

    let varflag = localStorage.getItem(j);
    varflag = varflag * 1;

    if (varflag !== 0) {
        alert("This question has already been answered. Tap 'OK' to navigate to next question");
        // navigate to next question //
        let navflag = (questionarray[i][2]);
        window.location.replace(navflag);
    }
});
