import React from 'react'

export default function Login() {

    const[name,setName]=useState([])
    useEffect(()=>{
         setName(['Dhanam','Dhanam123'])
     },[])
   
    const submitHandler=e=>{
        e.preventDefault();
    }
    Login(name);

    return (
        <form onSubmit={submitHandler}>
        <div className="form-inner">
            <h2>Login</h2>
         

            <div className="form-group">
            <label htmlFor='name'>Name:</label>
            <input type="text" name="name" id="name"/>
            <div className="form-group">
            <label htmlFor='name'>Password:</label>
            <input type="password" name="password" id="password"/>
            
            </div>
            <input type='submit' value="Login"/>
         

        </div>
        </div>
        </form>
    )
}
