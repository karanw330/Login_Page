function Validation() {
  let username = document.getElementById("exampleFormControlInput1").value.trim();
  let password = document.getElementById("exampleFormControlInput2").value.trim();

  let usernameError = "";
  let passwordError = "";

  if (username.length === 0) {
    usernameError = "Cannot leave a blank entry";
  } else if (username.length < 5) {
    usernameError = "Username is too short";
  }

  if (password.length === 0) {
    passwordError = "Cannot leave a blank entry";
  } else if (password.length < 8) {
    passwordError = "Minimum 8 characters are required in password";
  }

  document.getElementById("username-error").innerHTML = usernameError;
  document.getElementById("password-error").innerHTML = passwordError;
}