// jshint esversion: 6

// ********************************** Global Variables ********************************** //

//Set global variables - variables that are passed between functions //
var nextReveal = 0;
var nextRevealValue = 0;
var nextRevealWaste = 0;
var player;
var imageCount = 0;
var letterCount = 0;
var exampleStepNo = 1;
var getpage;

//Set global variables - flags to ensure all 8 images have been clicked before navigating from eightwastes.html //
var transportationFlag = 0;
var inventoryFlag = 0;
var motionFlag = 0;
var waitingFlag = 0;
var overproductionFlag = 0;
var overprocessingFlag = 0;
var defectsFlag = 0;
var skillsFlag = 0;

//Set global variables - array examplestep, answerindex and answertext for on example.html //
let examplearray = [
                    ['1. It`s first thing in the morning, and the Hygrometer is displaying:',  '1', 'Ventilating the room using: a fan, vents or a window WILL reduce the Humidity a bit, but this room is far too cold! Turning on the heating will not only make the room more comfortable, but it will heat the air, allowing the Humidity to reduce.'],
                    ['2. We turn the heating on and wait a short while. The Hygrometer is now displaying: <span class="orange-highlight">10&deg;C and 74%RH</span>',  '5', 'The room is still too cold - it would be uncomfortable to sit in, let alone worry about ventilation.'],
                    ['3. After a short while, the Hygrometer now displays: <span class="orange-highlight">19&deg;C and 56%RH</span>',  '2', 'The room is a comfortable temperature and the humidity is in the `ideal` range. Now is a good time to open the trickle vents to let air circulate.'],
                    ['4. The afternoon sun is shining into the room, keeping it at a toasty <span class="orange-highlight">24&deg;C</span>. You decide this is a good time to dry your laundry on a clothes horse.',  '4', 'Opening a window will allow the moisure that evaporates for the laundry to escape to the outside. It`s a good idea to keep the window open for a short while after the clothes are dry too.'],
                    ['5. Turn the chair upside-down to fit the seat-back.',  '4', 'The MOTION of turning the chair adds time. If we designed a fixture to hold the chair in place while we fit the legs and the seat-back, we could remove this.'],
                    ['6. Finally, we paint the chair.',  '1', 'Adding paint is changing the shape, so more VALUE is being added.'],
                    ['7. Last thing to do is to put the chair in the storeroom with all the others.',  '3', 'Creating INVENTORY is waste. Do we have orders for all the chairs in our storeroom? We should build to demand.']
                    ];

//Set global variables - flags for each of the dragcards on question-five.html //
var dragcard1 = null;
var dragcard2 = null;
var dragcard3 = null;
var dragcard4 = null;
var dragcard5 = null;

//Set global variables - flags for each of the questions in the test //
// 0 = incomplete, 1 = correct, -1 = incorrect //
var answerFlag1 = 0;
var answerFlag2 = 0;
var answerFlag3 = 0;
var answerFlag4 = 0;
var answerFlag5 = 0;
var answerFlag6 = 0;
var answerFlag7 = 0;
var answerFlag8 = 0;
var answerFlag9 = 0;
var answerFlag10 = 0;

//Set global variables - flags for each of the dragcards on question-five.html //
var dragcard1 = null;
var dragcard2 = null;
var dragcard3 = null;
var dragcard4 = null;
var dragcard5 = null;

//Set global variables - array for the contents of each of the orderboxes on question-nine.html //
let orderArray = [
                    ['orderbox1', 'ordercard1', 'delivering ahead of schedule', 'full'],
                    ['orderbox2', 'ordercard2', 'using the wrong resource', 'full'],
                    ['orderbox3', 'ordercard3', 'faults', 'full'],
                    ['orderbox4', 'ordercard4', 'moving the work/customer around', 'full'],
                    ['orderbox5', 'ordercard5', 'complicated processes', 'full'],
                    ['orderbox6', 'ordercard6', 'moving the worker around', 'full'],
                    ['orderbox7', 'ordercard7', 'queues', 'full'],
                    ['orderbox8', 'ordercard8', 'building up stock', 'full']
                    ];

//Set global variables - flags for each of the dragcards drop locations on question-five.html //
// 0 = unmoved, 1 = correct, -1 = incorrect //
var drag1Score = 0;
var drag1Score = 0;
var drag3Score = 0;
var drag4Score = 0;
var drag5Score = 0;


// ********************************** Global Functions ********************************** //

//Function: revealing the nextLink after content has been interacted with //
function revealNext() {
    $("#nextLink").removeClass("hidden");
    $("#nextLink").addClass("unhidden");
    $("#testanswerbtn").removeClass("hidden");
    $("#testanswerbtn").addClass("unhidden");
    
}

// ********************************** Unused - to be deleted ********************************** //

// Function: navigate to question-one.html from test-intro.html //
function goBegin() {
window.location.replace('question-one.html');
}