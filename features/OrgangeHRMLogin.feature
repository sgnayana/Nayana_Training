Feature: OrgangeHRM login page
        
    Scenario: Checking the functionality of login page with Valid username and password
        Given User navigate to the OrangeHRM Login page URL
        When User enters the valide username "admin" and password "admin123"
        And User clicks on the login button
        Then verify the user logged in successfully  

    Scenario: Checking the functionality of the PIM module
        When User navigates to the PIM module
        And User clicks on the Add Employee button
        And User enters the First Name and Last Name of the employee
        Then verify the employee added successfully
    
    