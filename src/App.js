import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

const handleSubmit = (item) => {
  this.toggle();
  if (item.id) {
    axios
      .put(`http://localhost:8000/api/gds/${item.id}/`, item)
      .then((res) => this.refreshList());
    return;
  }
  axios
    .post("http://localhost:8000/api/gds/", item)
    .then((res) => this.refreshList());
};

const handleDelete = (item) => {
  axios
    .delete(`http://localhost:8000/api/gds/${item.id}`)
    .then((res) => this.refreshList());
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
