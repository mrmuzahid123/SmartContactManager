from app.database.connection import get_session
from app.models.contact import Contact


def add_contact(
    first_name,
    last_name=None,
    phone=None,
    email=None,
    company=None,
    designation=None,
    address=None,
    birthday=None,
    notes=None
):
    session = get_session()

    try:
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            company=company,
            designation=designation,
            address=address,
            birthday=birthday,
            notes=notes
        )

        session.add(contact)
        session.commit()
        session.refresh(contact)

        return contact

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


# =========================
# GET ALL CONTACTS
# =========================

def get_all_contacts():

    session = get_session()

    try:
        contacts = (
            session.query(Contact)
            .order_by(Contact.created_at.desc())
            .all()
        )

        return contacts

    finally:
        session.close()

def delete_contact(contact_id):

    session = get_session()

    try:
        contact = session.get(Contact, contact_id)

        if contact:
            session.delete(contact)
            session.commit()
            return True

        return False

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()