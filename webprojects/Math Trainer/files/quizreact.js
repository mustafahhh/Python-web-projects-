
function App() {
    //Define
    const [Equation,setEquation] = React.useState(JSON.parse(PostData('http://127.0.0.1:8000/api/equation/1/'))["Equation"]);//The current equation
    const [Equations,setEquations] = React.useState([Equation]);//array of the equations so we can send it to server and then server gives us the answer
    const [Answered,setAnswered] = React.useState(0)//How much Equations you answered
    const [Answersarray,setAnswersArray] = React.useState([])
    //App
    return (
    <div>
    <header>
        <div>
            <h1>{Answered}/30</h1>
        </div>
    </header>
    <div>

            <Question level={localStorage.getItem('Level')} Answersarray={Answersarray} setAnswersArray={setAnswersArray} Equation={Equation} setEquation={setEquation} Equations={Equations} setEquations={setEquations} Answered={Answered} setAnswered={setAnswered} />

    </div>


    </div>

    );




}
function Question(props) { 






    const [answer,setAnswer] = React.useState('')
    const [Time,setTime] = React.useState(0)

    setInterval(() => {
        setTime(Time + 1)
    }, 1000);

    //LS = localStorage
    //Functions for LocalStorage easy controlling 
    function WriteLSArray(adress,data)
    {
        var a;
        //is anything in localstorage?
        if (localStorage.getItem(adress) === null) {
            a = [];
        } else {
            // Parse the serialized data back into an array of objects
            a = JSON.parse(localStorage.getItem(adress));
        }
        // Push the new data (whether it be an object or anything else) onto the array
        a.push(data);
        // Alert the array value
        // Re-serialize the array back into a string and store it in localStorage
        localStorage.setItem(adress, JSON.stringify(a));
    }




    //total time you needed to end the quiz and we will use it in data analytics in the http://127.0.0.1:8000/stats/charts/
    function SumbitAnswer() { 
        if (answer == "") { 
            var button = document.querySelector("#button")
            var BC = button.style.borderColor //BC = border Color
            button.style.color = "red"
            button.style.borderColor  = "red"
            button.addEventListener('transitionend', () => {
                button.style.color = "white"
                button.style.borderColor = BC 
            });
        
        
        }
        
        else if(props.Answered !== 30 ){ 
        //1-define new variables                 
        let NewEquation =  JSON.parse(PostData(`http://127.0.0.1:8000/api/equation/${props.level}/`))["Equation"]
        let NewEquationarr = [NewEquation,...props.Equations ]
        let NewAnswersarr = [answer, ...props.Answersarray]
        //2-set the new variables
        
        props.setAnswersArray(NewAnswersarr)
        props.setAnswered(props.Answered + 1)
        if (props.Answered !==  30 ) { 
        props.setEquation(NewEquation)
        props.setEquations(NewEquationarr)
    }




        setAnswer('')
        document.querySelector("#AnswersInput").focus()
    }



    if (props.Answered == 30){
        console.log([answer,...props.Answersarray])

        //1-Send the equations list and get answers
        const answers = PostData(`http://127.0.0.1:8000/api/CheckQuestions/`,"POST", `{"Equations":"${props.Equations}","Answers":"${[answer,...props.Answersarray]}"}`)
        //2-Use the data 

        console.log(answers)
        var TotalAnswers = localStorage.getItem('TotalAnswers')
        var TotalRounds = localStorage.getItem('TotalRounds')

        ////////////////////    Add data    ///////////////////////////

        localStorage.setItem("TotalAnswers",parseInt(TotalAnswers)+parseInt(JSON.parse(answers)["Answered"]))
        localStorage.setItem("TotalRounds",parseInt(TotalRounds)+1)
        WriteLSArray('Answers',answer)
        WriteLSArray('Time',Time)


        var TotalAnswers = localStorage.getItem('TotalAnswers')
        var TotalRounds = localStorage.getItem('TotalRounds')
        localStorage.setItem("AR",(parseInt(TotalAnswers)/parseInt(TotalRounds)).toFixed(2))//calculate


        //We made the answers array so we can make graphs and use it to change equations level
       // window.location = `http://127.0.0.1:8000/answers/${JSON.parse(answers)["Answered"]}/`
    }
    }

    return(
    <div className='questionshandler'>
            <div className='EquationBox'>
                {props.Equation.split(' ').map((word) => (<div className='Equation'>{word}</div>))}


            </div>
            <input id="AnswersInput" onChange={e => setAnswer(e.target.value)} autoFocus value={answer} type='number' placeholder='answer'/>
            <button id="button" onClick={SumbitAnswer}>Sumbit</button>
    </div>
    );

}


ReactDOM.render(<App  />, document.querySelector('body'))
