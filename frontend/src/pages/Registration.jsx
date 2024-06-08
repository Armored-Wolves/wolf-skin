import Form from "../components/Form";

function Registration() {

    return <>
        <Form route="http://127.0.0.1:8000/api/user/register" method="registration"></Form>
    </>
}

export default Registration;