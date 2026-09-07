from src.customer import Customer, update_customer_email


def test_update_customer_email_preserves_id_and_audit():
    customer = Customer(10, "Ana", "ana@example.com", "admin", "admin")
    updated = update_customer_email(customer, "NEW@example.com", "agent")

    assert updated.customer_id == 10
    assert updated.created_by == "admin"
    assert updated.updated_by == "agent"
    assert updated.email == "new@example.com"


def test_invalid_email_is_rejected():
    customer = Customer(10, "Ana", "ana@example.com", "admin", "admin")

    try:
        update_customer_email(customer, "invalid", "agent")
        assert False
    except ValueError as exc:
        assert str(exc) == "invalid-email"


def test_various_invalid_email_formats_raise_value_error():
    customer = Customer(10, "Ana", "ana@example.com", "admin", "admin")
    invalid_emails = [
        "",
        "   ",
        "plainaddress",
        "@missingusername.com",
        "username@.com",
        "username@com",
        "username@domain..com",
        "username@domain.com.",
        "user name@domain.com",
        "username@domain .com",
        None,
        12345,
    ]

    for email in invalid_emails:
        try:
            update_customer_email(customer, email, "agent")
            assert False, f"Expected ValueError for email: {email}"
        except ValueError as exc:
            assert str(exc) == "invalid-email"


def test_complex_valid_email_formats():
    customer = Customer(10, "Ana", "ana@example.com", "admin", "admin")
    valid_emails = [
        ("user.name+tag@domain.co.uk", "user.name+tag@domain.co.uk"),
        ("FIRST.LAST@SUB.DOMAIN.ORG", "first.last@sub.domain.org"),
        ("custom_er-123@my-domain.net", "custom_er-123@my-domain.net"),
    ]

    for input_email, expected_email in valid_emails:
        updated = update_customer_email(customer, input_email, "agent")
        assert updated.email == expected_email