Layer mesh : cells:2448671  faces:7631162  points:2761126
Cells per refinement level:
    0	17328
    1	4058
    2	12012
    3	44996
    4	1632997
    5	158028
    6	579252

-- Blockmesh -- 
blocks
(
    hex (0 1 2 3 4 5 6 7) (20 30 30) simpleGrading (1 1 1)
);

-- snappyHexMeshDict --

refinementSurfaces
{
    outlet
    {
        level (3 4);
    }

    motorBike
    {
        // Surface-wise min and max refinement level
        level (5 6);

        // Optional specification of patch type (default is wall). No
        // constraint types (cyclic, symmetry) etc. are allowed.
        patchInfo
        {
            type wall;
            inGroups (motorBikeGroup);
        }
    }
}


