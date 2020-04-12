import React, {Fragment} from 'react';
import {connect} from 'react-redux';

import {accessoriesActions, userActions} from "../_actions";
import {Loader} from "../_components";

import {Datatable} from "@o2xp/react-datatable";

// https://github.com/o2xp/react-datatable
const getOptions = (data) => ({
    keyColumn: "id",
    dimensions: {
        datatable: {
            height: "500px",
            width: "100%",
        },
    },
    data: {
        columns: [
            {
                id: "name",
                label: "Kostým",
                colSize: "100px",
            },
            {
                id: "manufacturer",
                label: "Výrobce",
                colSize: "80px",
            },
            {
                id: "material",
                label: "Materiál",
                colSize: "50px",
            },
            {
                id: "size",
                label: "Velikost",
                colSize: "20px"
            },
            {
                id: "count",
                label: "Počet kusů",
                colSize: "20px"
            },
            {
                id: "price",
                label: "Cena",
                colSize: "20px"
            },
            {
                id: "color",
                label: "Barva",
                colSize: "80px"
            },
            {
                id: "wear_level",
                label: "Opotřebení",
                colSize: "50px"
            },
            {
                id: "action",
                label: "Akce",
                dataType: "action",
                colSize: "160px",
            }
        ],
        rows: data.map((d) => ({
            name: d.name,
            manufacturer: d.manufacturer,
            material: d.material,
            size: d.size,
            count: d.count,
            price: d.price,
            color: d.color,
            wear_level: d.wear_level,
            action: d.id,
        }))

    }
});

const createCustomDataTypes = (dispatch) => [
    {
        dataType: "action",
        component: id => <Fragment>
            <button onClick={() => dispatch(accessoriesActions.deleteAcc(id))} className="btn btn-primary">Editovat</button>
            <button onClick={() => dispatch(accessoriesActions.deleteAcc(id))} className="btn btn-danger">Odstranit</button>
        </Fragment>,
    }
]


class ManageAccessoriesPage extends React.Component {
    constructor(props) {
        super(props);

        const {dispatch, loggedIn} = this.props;
        if (!loggedIn)
            dispatch(userActions.logout());
    }

    componentDidMount() {
        this.props.dispatch(accessoriesActions.getAll());
    }

    render() {
        const {items = [], loading, dispatch} = this.props;


        console.log("Loading: ", loading);

        return (loading ? (
                <Loader/>
            ) : (
                <Fragment>
                    <h1>Počet doplňků {items.length}</h1>
                    <Datatable
                        options={getOptions(items)}
                        customDataTypes={createCustomDataTypes(dispatch)}
                    />
                </Fragment>
            )
        );
    }
}

function mapStateToProps(state) {
    const {items, loading} = state.accessories;
    const {loggedIn} = state.authentication;
    return {
        loading,
        items,
        loggedIn,
    }
}

export default connect(mapStateToProps)(ManageAccessoriesPage);