
var copyBtn = document.querySelector('.copyBtn')


function generatePassword () {
  var chars = "abcdefghijklmnABCoZ!@#$%^xyz012345678MpqrsDLEF0AZ!@#$%^BCODtKuvJwIG{}[]Hxyz01234567890AZ!@#$%^BCODEFGHNIJKLMNOPQRSTUVWXYZ!@#$%^%^&*()?"
  var passwordLength = 35;
  var password = " ";

  for (var i = 0; i<passwordLength; i++){
    var randomNumber = Math.floor(Math.random() * chars.length);
    password += chars.substring(randomNumber, randomNumber+1);
  }

  document.getElementById('password').value = password;
  copyBtn.innerHTML = "New Password Copied: <br>" + password;
}


function copyPassword () {
  var copyText = document.getElementById('password');
  copyText.select();
  copyText.setSelectionRange(0,9999);
  document.execCommand("copy");
  alertBox.getElementById('#copyBtn').toggle('active');

}

function alertMsg() {
  alert("Password Copied");
}