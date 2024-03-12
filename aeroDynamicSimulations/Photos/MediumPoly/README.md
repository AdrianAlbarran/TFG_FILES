Layer mesh : cells:896636  faces:2802366  points:1021235    
Cells per refinement level:
    0	4188
    1	2128
    2	7809
    3	24865
    4	471386
    5	58744
    6	327516


-- Blockmesh -- 
blocks
(
    hex (0 1 2 3 4 5 6 7) (20 30 30) simpleGrading (1 1 1)
);


-- snappyHexMeshDict --

refinementSurfaces
{
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

