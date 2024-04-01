word myZone = "testExplicit";
label zoneID = mesh.cellZones().findZoneID(myZone);

vector myVector(1e3, 0, 0);

const labelList& cells = mesh.cellZones()[zoneID];
forAll(cells, i)
{
const label cell = cells[i];
explicitSourceU[cell] = myVector; //keep in mind that you need to match Unit also!
}
