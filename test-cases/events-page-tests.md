# Test Cases for GreenCity Events Page

### Test Case ID: 1
### Title: Verify successful registration with valid data

**Preconditions:**
- The page https://www.greencity.cx.ua/#/greenCity/events is opened
- The user is not logged in
- The user is not registered in the system

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click "Sign Up" in the header menu | - | Registration form is displayed |
| 2 | Enter email into "Email" field | example321@gmail.com | Value is successfully entered into the field |
| 3 | Enter username into "Username" field | Yurii | Value is successfully entered into the field |
| 4 | Enter password into "Password" field | Qwerty1! | Value is successfully entered into the field |
| 5 | Enter password into "Confirm Password" field | Qwerty1! | "Sign Up" button becomes active |
| 6 | Click "Sign Up" button | - | Success message is displayed |

---

### Test Case ID: 2
### Title: Verify successful sign in with valid data

**Preconditions:**
- The page https://www.greencity.cx.ua/#/greenCity/events is opened
- The user is registered in the system
- The user is not logged in

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click "Sign In" button in the header menu | - | Login form is displayed |
| 2 | Enter email into "Email" field | example321@gmail.com | Value is successfully entered into the field |
| 3 | Enter password into "Password" field | Qwerty1! | Value is successfully entered into the field |
| 4 | Click "Sign In" button | - | User is redirected to the profile page (URL contains /profile/) |

---

### Test Case ID: 3
### Title: Verify that the "Create Event" button functions correctly

**Preconditions:**
- The page https://www.greencity.cx.ua/#/greenCity/events is opened
- The user is logged in

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click the "Create Event" button | - | User is redirected to the "Create Event" page (URL contains /events/create-update-event) |

---

## Additional task

### Test Case ID: 4
### Title: Verify registration is not possible with invalid data

**Preconditions:**
- The page https://www.greencity.cx.ua/#/greenCity/events is opened
- The user is not logged in
- The user is not registered in the system

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click "Sign Up" in the header menu | - | Registration form is displayed |
| 2 | Enter invalid email into "Email" field | example.gmail.com | Validation error message is displayed in red under the field |
| 3 | Enter invalid username into "Username" field | 123 | Validation error message is displayed in red under the field |
| 4 | Enter invalid password into "Password" field | 123 | Validation error message is displayed in red under the field |
| 5 | Enter password into "Confirm Password" field | 123 | Validation error message is displayed in red under the field |
| 6 | Observe "Sign Up" button | - | "Sign Up" button remains disabled |

