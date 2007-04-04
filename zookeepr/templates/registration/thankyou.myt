<h2>Registration</h2>

<h3>Thank You</h3>

<p>
Thank you for your registration! 
</p>

<p>
An email has been sent to you at <em><% c.person.email_address | h %></em> with details of your registration.  To complete the registration process (allowing you to log in again to modify your details and pay your invoice) please follow the instructions in that message.
</p>

</p>
<p>
If you do not receive this message in a reasonable timeframe, please contact us at <% h.ctte_email() %>
</p>

<p>
<a href="<% h.url_for("home") %>">Click here</a> to return to the main page.
</p>
