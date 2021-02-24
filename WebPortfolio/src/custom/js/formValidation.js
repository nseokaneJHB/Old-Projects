//=========================== Validate Full Name =========================================
function validateName() {

    var myFName = document.getElementById("fname").inputMode;
    if (!myFName.includes(" ")) {
        alert("Please include your second name");
        //document.getElementById("msgName").innerHTML = "Please include your second name";
        //document.getElementById("fname").item.style.color = "#FF3300";
        return false;
    }

}

//=========================== Validate Email Address =========================================

//JavaScript code for validating email format
function ValidateEmail(uemail) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (uemail.value.match(mailformat)) {
        return true;
    } else {
        alert("You email must contain '@' and a domain at the end");
        uemail.focus();
        return false;
    }
}

//=========================== Validate Phone number =========================================
function validatePhone() {

    var myPhone = document.getElementById("num").inputMode;
    if (!myPhone.includes("@")) {
        //alert("Please include your second name");
        document.getElementById("msgNum").innerHTML = "Your number has to be 10 digits";
        return false;
    }

}

//=========================== Validate Password =========================================
function validatePassword() {

    var myPass = document.getElementById("pass").inputMode;
    if (!myPass.includes("@")) {
        //alert("Please include your second name");
        document.getElementById("msgPass").innerHTML = "Your passwords have to match";
        return false;
    }

}

//=========================== Validate Occupation =========================================
function validateOccupation() {

    var myOcc = document.getElementById("occ").inputMode;
    if (myOcc.length == 0) {
        //alert("Please include your second name");
        document.getElementById("msgOcc").innerHTML = "You have to select at least one occupation";
        return false;
    }

}

function validatingOtherFunctions() {

}