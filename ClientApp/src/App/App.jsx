import React from 'react';
import {Router, Route} from 'react-router-dom';
import {connect} from 'react-redux';

import {history} from '../_helpers';
import {alertActions} from '../_actions';
//import {PrivateRoute} from '../_components';
import {HomePage} from '../HomePage';
import {LoginPage} from '../LoginPage';
import {RegisterPage} from '../RegisterPage';

import {Navbar} from "../_components";
import {CostumesPage} from "../CostumesPage";
import {AccessoriesPage} from "../AccessoriesPage";
import ProfilePage from "../ProfilePage/ProfilePage";
import {MyOrdersPage} from "../OrdersPage";

class App extends React.Component {
    constructor(props) {
        super(props);

        const {dispatch} = this.props;
        history.listen((location, action) => {
            // clear alert on location change
            dispatch(alertActions.clear());
        });
    }

    render() {
        const {alert} = this.props;
        return (
            <div className="jumbotron">
                <div className="container">
                    <Router history={history}>
                        <Navbar/>
                        <div className="col-sm-12">
                            {alert.message &&
                            <div className={`alert ${alert.type}`}>{alert.message}</div>
                            }

                            <div>
                                <Route exact path="/" component={HomePage} />
                                <Route path="/home" component={HomePage}/>

                                <Route path="/login" component={LoginPage}/>
                                <Route path="/register" component={RegisterPage}/>

                                <Route path="/profile" component={ProfilePage} />
                                <Route path="/orderHistory" component={MyOrdersPage} />

                                <Route path="/costumes" component={CostumesPage}/>
                                <Route path="/accessories" component={AccessoriesPage}/>
                            </div>
                        </div>
                    </Router>
                </div>
            </div>
        );
    }
}

function mapStateToProps(state) {
    const {alert} = state;
    return {
        alert
    };
}

const connectedApp = connect(mapStateToProps)(App);
export {connectedApp as App};